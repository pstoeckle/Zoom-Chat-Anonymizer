# Zoom Chat Anonymizer

```bash
$ zoom-chat-anonymizer --help                      
Usage: zoom-chat-anonymizer [OPTIONS] COMMAND [ARGS]...

  Helpful script to process Zoom chats.

Options:
  --version  Version
  --help     Show this message and exit.

Commands:
  anonymize-zoom-chats       Anonymize Zoom chats.
  create-html-from-markdown  Create HTML files from the markdown files.
```

## Anonymize Zoom Chats

```bash
$ zoom-chat-anonymizer anonymize-zoom-chats --help
Usage: zoom-chat-anonymizer anonymize-zoom-chats [OPTIONS]

  Anonymize Zoom chats.

Options:
  -o, --output_folder DIRECTORY
  -i, --input_folder DIRECTORY
  -t, --tutor TEXT
  --help                         Show this message and exit.
```

## Create HTML from Markdown

```bash
$ zoom-chat-anonymizer create-html-from-markdown --help
Usage: zoom-chat-anonymizer create-html-from-markdown [OPTIONS]

  Create HTML files from the markdown files.

Options:
  --bib_file FILE
  -i, --input_folder DIRECTORY
  --help                        Show this message and exit.
```
