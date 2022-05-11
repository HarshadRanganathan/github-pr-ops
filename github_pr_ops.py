import json
import sys
from types import SimpleNamespace
import utils
import properties
from jinja2 import Environment, FileSystemLoader
from jinja2.exceptions import TemplateError, TemplateNotFound
from pull_request import PullRequest
from datetime import datetime


env = Environment(loader=FileSystemLoader('./templates'))


def get_open_prs_by_org(org_name: str = ''):
    """
    Function to retrieve PRs under a specified Git Hub Org and send an email if any Open PRs found.
    :param org_name: Github organisation name for all repo to be searched under
    """

    open_pr_list = []

    url = "".join([properties.GITHUB_BASE_URL, properties.SEARCH, properties.ISSUES_AND_PRS_RESOURCE, properties.QUERY])

    if org_name != '':

        open_pr_query_string = properties.OPEN_PR_QUERY
        open_pr_query_string = open_pr_query_string.format(org_name=org_name)

        url += 'q={query_string}'.format(query_string=open_pr_query_string)
        url += '&per_page=100&page={page_number}'

        print(url)

        open_pr_list = utils.retrieve_data(url)

        pr_data = []

        for each in open_pr_list:
            pr_json_obj = json.loads(json.dumps(each), object_hook=lambda d: SimpleNamespace(**d))

            days_since = utils.get_num_days(utils.get_date(pr_json_obj.created_at), datetime.now())

            pr_data.append(PullRequest(pr_json_obj.title, pr_json_obj.html_url, pr_json_obj.user.login, days_since))

        try:
            tmpl = env.get_template('pr_html_tmpl.jinja')

            with open("pr_file.html", "w") as fh:
                fh.write(tmpl.render(data=pr_data))

        except (TemplateNotFound, TemplateError) as err:
            print(f'Error: {type(err)} {err}', file=sys.stderr)

    else:
        print("search pattern or organisation name illegal, please make sure only alphabets are passed!")

    return open_pr_list


if __name__ == '__main__':
    get_open_prs_by_org(properties.ORG_NAME)
