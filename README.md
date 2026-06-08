# Robert Henderson Website

This website is generated using [Pelican](https://getpelican.com/), a static site generator written in Python. It was migrated from the deprecated `pygreen` generator.

## Project Structure

*   `content/`: Contains the source Markdown files.
    *   `content/pages/`: Static pages like the home page (`index.md`).
    *   `content/papers/`: Individual paper entries.
*   `theme/rhenderson/`: Custom Bootstrap-based Pelican theme.
*   `resources/`: Static assets like PDFs and CV (mirrored in `content/resources/` for Pelican processing).
*   `pelicanconf.py`: Main configuration file for development.
*   `publishconf.py`: Configuration for production/publication.
*   `tasks.py`: Automation tasks for building and deploying (using `invoke`).

## Local Development

1.  **Environment Setup:**
    ```bash
    source venv/bin/activate
    pip install pelican markdown boto3 invoke
    ```

2.  **Build the site:**
    ```bash
    pelican content
    # OR
    invoke build
    ```

3.  **Preview the site:**
    ```bash
    pelican --listen
    # OR
    invoke serve
    ```
    Visit `http://localhost:8000` in your browser.

## Content Management

### Adding a New Paper
Add a new `.md` file to `content/papers/` with the following metadata at the top:
```markdown
Title: My Paper Title
Date: YYYY-MM-DD
Category: Papers
Slug: my-paper-slug
```

### Updating the Home Page
Modify `content/pages/index.md`.

## Deployment

To deploy the site to an AWS S3 bucket:
```bash
invoke s3_upload --bucket-name=your-s3-bucket-name
```
Ensure your AWS CLI is configured with the necessary permissions.
