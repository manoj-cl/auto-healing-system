## Troubleshooting & Lessons Learned

During development of the **Python Auto-Healing System**, several real-world DevOps challenges were encountered while containerizing and running the application using Docker and Docker Compose.

---

### 1. Python Version Conflict on macOS

**Issue**

After installing a newer Python version, the system still showed:

```
python3 --version
Python 3.9.6
```

**Cause**

macOS includes a system Python installed via developer command-line tools, which takes precedence in the system PATH.

**Resolution**

Installed Python using Homebrew and used a virtual environment.

```
brew install python
```

---

### 2. Docker Container Running but No Logs Appearing

**Issue**

The container started successfully but running:

```
docker logs <container>
```

showed no output.

**Cause**

The logger was configured to write logs only to a **file**, while Docker only captures **stdout/stderr** output.

**Resolution**

Added a **console handler** to send logs to stdout.

---

### 3. Duplicate Log Entries

**Issue**

Running the script locally produced duplicate log lines.

**Example**

```
CPU=5.4% MEM=53.3%
CPU=5.4% MEM=53.3%
```

**Cause**

Multiple logging handlers were initialized.

**Resolution**

Added a check to prevent multiple handlers from being added to the logger.

```
if logger.handlers:
    return logger
```

---

### 4. Logs Not Visible on Host Machine

**Issue**

The application generated logs inside the container but the host system log file was not updated.

**Cause**

Docker containers run with an **isolated filesystem**.

Logs were written inside the container:

```
/app/logs/auto_heal.log
```

but not visible on the host.

**Resolution**

Used a **bind mount** to map the container log directory to the host.

```
docker run -d \
--name auto-healer \
-v $(pwd)/logs:/app/logs \
auto-healer
```

This maps:

```
Host Directory:      ./logs
Container Directory: /app/logs
```

---

### 5. Logs Not Showing When Using Docker Compose

**Issue**

When running:

```
docker compose up
```

the container started but no logs appeared in the terminal.

**Cause**

The logging configuration only wrote to a file. Docker Compose shows logs only from **stdout/stderr**.

**Resolution**

Modified the logger to output logs to both:

* log file
* console

---

### Logger Code Changes

The original logger only wrote to a file:

```python
logging.basicConfig(
    filename=log_dir / "auto_heal.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
```

To support Docker logging, a **console handler** was added.

**New Logger Implementation**

```python
from pathlib import Path
import logging
import sys

def setup_logger():
    log_dir = Path("/app/logs")
    log_dir.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers
    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    # File handler
    file_handler = logging.FileHandler(log_dir / "auto_heal.log")
    file_handler.setFormatter(formatter)

    # Console handler (Docker logs)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
```

Now logs are written to both:

```
/app/logs/auto_heal.log
```

and

```
docker logs
docker compose up
```

---

### Key Concepts Learned

This project provided hands-on experience with:

* Python structured logging
* Docker containerization
* Docker filesystem isolation
* Bind mounts and volume mapping
* Docker Compose logging behavior
* Debugging containerized applications
* Troubleshooting workflow