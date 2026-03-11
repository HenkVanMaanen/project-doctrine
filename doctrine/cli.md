# CLI Design

## Standards

- POSIX Utility Conventions: https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap12.html
- GNU Argument Syntax: https://www.gnu.org/software/libc/manual/html_node/Argument-Syntax.html

Applies to: CLI

## Requirements

### Exit Codes

- Exit codes MUST follow conventions:
  - `0` — success
  - `1` — general error
  - `2` — usage/argument error
  - `126` — command not executable
  - `127` — command not found
- Custom exit codes MUST be documented and MUST use the range 3–125.
- Reference: POSIX exit status and [BSD sysexits](https://man.freebsd.org/cgi/man.cgi?query=sysexits&sektion=3).

### Argument Parsing

- Arguments MUST follow POSIX/GNU conventions:
  - Short flags: `-v`, `-f file`
  - Long flags: `--verbose`, `--file=path`
  - `--` MUST end option parsing
  - `-h` / `--help` MUST display usage
  - `--version` MUST display version
- Subcommands MUST be used for distinct operations (e.g., `tool create`, `tool list`).

### Input/Output

- Normal output MUST go to stdout.
- Errors and diagnostics MUST go to stderr.
- When stdout is not a TTY (piped), output MUST be machine-parseable (no colors, no progress bars).
- A `--json` or `--output=json` flag SHOULD be provided for structured output.
- A `--quiet` / `-q` flag MUST suppress non-essential output.
- A `--verbose` / `-v` flag MUST enable detailed output.

### Signal Handling

- `SIGINT` (Ctrl+C) MUST trigger graceful shutdown and cleanup.
- `SIGPIPE` MUST be handled silently (no error when piped output is closed).
- `SIGTERM` MUST be handled identically to `SIGINT`.
- Cleanup MUST occur on all exit paths (temp files, locks, resources).

### Color and Formatting

- Color output MUST respect the `NO_COLOR` environment variable (https://no-color.org/).
- Color MUST be disabled when stdout is not a TTY.
- Progress indicators MUST be used for long-running operations (when TTY).
- Progress indicators MUST NOT pollute output when piped.

### Shell Completion

- Shell completion scripts SHOULD be generated for bash, zsh, and fish.

### Configuration

- Config file locations MUST follow the XDG Base Directory Specification (https://specifications.freedesktop.org/basedir-spec/latest/).
  - Config: `$XDG_CONFIG_HOME/<app>/` (default `~/.config/<app>/`)
  - Data: `$XDG_DATA_HOME/<app>/` (default `~/.local/share/<app>/`)
  - Cache: `$XDG_CACHE_HOME/<app>/` (default `~/.cache/<app>/`)
- Environment variables MUST override config file values.
- Config file format MUST be documented.

## See Also

- `architecture.md` — vertical slices, error handling
- `telemetry.md` — structured logging for CLI operations
- `testing.md` — CLI integration tests
- `versioning.md` — `--version` flag output

## Output Requirements

The generated architecture doc MUST include CLI-specific sections that:

- Define the command and subcommand structure
- Define exit codes with meanings
- Specify signal handling behavior
- Define output modes (human, JSON, quiet, verbose)
- Specify config file location and format
