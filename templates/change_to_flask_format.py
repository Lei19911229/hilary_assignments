import re

# Path to your file
file_path = 'index-2.html'

# CSS
# Read the file
# with open(file_path, 'r') as file:
#     content = file.read()

# # Regular expression to find the href value in the <link> tag
# pattern = r'<link rel="stylesheet" href="(css/.*?\.css)">'

# # Function to replace the href with the url_for format
# def replace_with_url_for(match):
#     css_file = match.group(1)  # Extract the file path, e.g., 'css/bootstrap.min.css'
#     # Construct the new string using url_for
#     return f'<link rel="stylesheet" href="{{{{ url_for(\'static\', filename=\'{css_file}\') }}}}">'

# # Use re.sub with the custom function to replace the href dynamically
# updated_content = re.sub(pattern, replace_with_url_for, content)

# # Write the updated content back to the file
# with open(file_path, 'w') as file:
#     file.write(updated_content)

# print("Replacement completed successfully!")



# img
# import re

# # Path to your file
# file_path = 'index-2.html'

# # Read the file
# with open(file_path, 'r') as file:
#     content = file.read()

# # Regular expression to match <img> tag with src and optional alt attribute
# pattern = r'<img src="(.*?)"( alt=".*?")?>'

# # Function to replace the src with url_for and remove any alt attribute
# def replace_with_url_for(match):
#     img_file = match.group(1)  # Extract the src file path
#     # Construct the new <img> tag without the alt attribute
#     return f'<img src="{{{{ url_for(\'static\', filename=\'{img_file}\') }}}}">'

# # Use re.sub with the custom function to replace the src and remove any alt attribute
# updated_content = re.sub(pattern, replace_with_url_for, content)

# # Write the updated content back to the file
# with open(file_path, 'w') as file:
#     file.write(updated_content)

# print("Replacement of <img src> and removal of any alt attribute completed successfully!")


# import re

# # Path to your file
# file_path = 'index-2.html'

# # Read the file
# with open(file_path, 'r') as file:
#     content = file.read()

# # Regular expression to find the background image URL in style="background: url(...)"
# pattern = r'background:\s?url\((.*?)\)'

# # Function to replace the background URL with url_for
# def replace_with_url_for(match):
#     img_file = match.group(1)  # Extract the file path from the background URL
#     # Construct the new background URL using url_for
#     return f'background: url("{{{{ url_for(\'static\', filename=\'{img_file}\') }}}}")'

# # Use re.sub with the custom function to replace the background URLs dynamically
# updated_content = re.sub(pattern, replace_with_url_for, content)

# # Write the updated content back to the file
# with open(file_path, 'w') as file:
#     file.write(updated_content)

# print("Replacement of background URLs completed successfully!")

import re

# Path to your file
file_path = 'index-2.html'

# Read the file
with open(file_path, 'r') as file:
    content = file.read()

# Regular expression to match the <script src="..."> tag
pattern = r'<script src="(.*?)"></script>'

# Function to replace the src with the url_for format
def replace_with_url_for(match):
    script_file = match.group(1)  # Extract the file path from the src attribute
    # Construct the new <script> tag using url_for
    return f'<script src="{{{{ url_for(\'static\', filename=\'{script_file}\') }}}}"></script>'

# Use re.sub with the custom function to replace the src dynamically
updated_content = re.sub(pattern, replace_with_url_for, content)

# Write the updated content back to the file
with open(file_path, 'w') as file:
    file.write(updated_content)

print("Replacement of <script src> completed successfully!")



