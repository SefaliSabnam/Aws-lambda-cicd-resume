import json

def lambda_handler(event, context):
    html_content = """<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>My Resume</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            padding: 20px;
            background-color: #f4f4f4;
        }
        .container {
            max-width: 800px;
            background: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }
        h1, h2 {
            color: #333;
        }
        .header {
            text-align: center;
            margin-bottom: 20px;
        }
        .profile img {
            width: 120px;
            height: 120px;
            border-radius: 50%;
            object-fit: cover;
        }
        .section {
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class=\"container\">
        <div class=\"header\">
            <h1>Sefali Sharon Sabnam</h1>
            <p> Software Engineer | DevOps Engineer</p>
        </div>

        <div class=\"profile\" style=\"text-align: center;\">
            <img src=\"https://assets.onecompiler.app/438v576hj/438v5ph8r/rony.jpg\" alt=\"Profile Picture\">
        </div>

        <div class=\"contact-info\">
            <h2>Contact Information</h2>
            <p>Email: sefali.sabnam26@gmail.com</p>
            <p>Phone: +123 456 7890</p>
            <p>LinkedIn: <a href=\"https://www.linkedin.com/in/sefali-sharon-sabnam-621372187/?trk=opento_sprofile_topcard\" target=\"_blank\">linkedin.com/in/sefali-sharon-sabnam</a></p>
            <p>GitHub: <a href=\"https://github.com/SefaliSabnam\" target=\"_blank\">github.com/SefaliSabnam</a></p>
        </div>

        <div class=\"section\">
            <h2>Experience</h2>
            <p><strong>Software Engineer</strong> - Digi-soft Tech (2024 - Present)</p>
            <p>Developed web applications using React and Node.js.</p>
            <p><strong>Intern Developer</strong> - XYZ Corp (2021 - 2022)</p>
            <p>Assisted in backend development using Python.</p>
        </div>

        <div class=\"section\">
            <h2>Education</h2>
            <p><strong>Bachelor</strong> - KMBB COLLEGE OF TECHNOLOGY (2014 - 2017)</p>
        </div>

        <div class=\"section\">
            <h2>Skills</h2>
            <ul>
                <li>Java, Selenium, Automation</li>
                <li>Python</li>
                <li>AWS, Git, Docker</li>
                <li>SQL</li>
            </ul>
        </div>

        <div class=\"section\">
            <h2>Projects</h2>
            <p><strong>Portfolio Website</strong> - <a href=\"https://www.linkedin.com/in/sefali-sharon-sabnam-621372187/?trk=opento_sprofile_topcard\" target=\"_blank\">View on LinkedIn</a></p>
            <p>Designed and built a personal portfolio using HTML, CSS, and JavaScript.</p>
            <p><strong>PIPELINE PROJECT</strong> - <a href=\"https://github.com/SefaliSabnam\" target=\"_blank\">View on GitHub</a></p>
            <p>Developed a pipeline project with multi-branch.</p>
        </div>
    </div>
</body>
</html>"""
    
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/html"},
        "body": html_content
    }
