import json
import requests


def get_jobs():
    # api call
    api_url = 'https://feed.jobylon.com/feeds/7d7e6fd12c614aa5af3624b06f7a74b8/?format=json'
    headers = {'Content-Type': 'application/json'}
    __response__ = requests.get(api_url, headers=headers)

    # return to client a simpler object
    print('entrou jobs')
    data = __response__.json()
    jobs = []
    for job in data:
        job = dict(
            # using get so we dont get an run time error in case the key is missing
            id=job.get('id'),
            company=dict(
                name=job.get('company').get('name'),
                website=job.get('company').get('website'),
                industry=job.get('company').get('industry'),
                logo=job.get('company').get('logo'),
                descr=job.get('company').get('descr'),
            ),
            title=job.get('title'),
            descr=job.get('descr'),
            function=job.get('function'),
            experience=job.get('experience'),
            employment_type=job.get('employment_type'),
            locations=job.get('locations'),
            ad=job.get('urls').get('ad'),
            apply=job.get('urls').get('apply'),

        )
        jobs.append(job)
    return jobs
