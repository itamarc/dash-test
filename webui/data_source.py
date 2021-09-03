import pandas as pd


def get_jobs_by_location(job_title, start_date, end_date) -> pd.DataFrame:
    """
    Return a list of jobs in the database that are in the location specified
    """
    data = [
        {
            'country': 'nl',
            'job_offers': 321
        },
        {
            'country': 'uk',
            'job_offers': 123
        },
        {
            'country': 'pt',
            'job_offers': 12
        },
        {
            'country': 'it',
            'job_offers': 23
        },
    ]
    # The data above did not work as is
    jobs_df = pd.DataFrame([])
    return jobs_df
