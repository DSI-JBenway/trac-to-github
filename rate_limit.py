from github import Github
import configparser

config = configparser.ConfigParser()
config.read('migrate.cfg')
github_token =  config.get('target', 'token')
github_api_url = config.get('target', 'url')
gh = Github(github_token, base_url=github_api_url)
limit = gh.get_rate_limit()
print(limit)