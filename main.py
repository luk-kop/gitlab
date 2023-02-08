import os

import gitlab
from dotenv import load_dotenv


def get_gitlab(private_token: str, url: str = '') -> gitlab.client.Gitlab:
    if url:
        return gitlab.Gitlab(url=url, private_token=private_token)
    return gitlab.Gitlab(private_token=private_token)


if __name__ == '__main__':
    load_dotenv('.env')

    GL_PRIVATE_TOKEN = os.environ.get('GL_PRIVATE_TOKEN')
    gl = get_gitlab(private_token=GL_PRIVATE_TOKEN)

    projects = gl.projects.list(owned=True)
    for project in projects:
        print(f'name: {project.name}, path: {project.path_with_namespace}, url: {project.web_url}')



