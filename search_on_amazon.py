from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type
import logging


class SearchOnAmazonInput(BaseModel):
    query: str = Field(..., description="A string variable identyfing the query to search on amazon; cannot be empty.")


class SearchOnAmazonTool(BaseTool):
    """
    Search On Amazon Tool
    """
    name: str = "Search On Amazon Tool"
    description: str = "Allows searching for products on Amazon"
    args_schema: Type[BaseModel] = SearchOnAmazonInput

    def _execute(self, query: str = None):
        return self.search_products_on_amazon(query=query)

    def search_products_on_amazon(self, query: str):
        try:
            import requests
            url = 'https://api.scraperapi.com/structured/amazon/search'
            payload = {
                'api_key': self.get_tool_config('API_KEY'),
                'query': query,
                'country': self.get_tool_config('COUNTRY').lower(),
                'tld': self.get_tool_config('TLD').lower(),
            }
            logging.info(f"Calling {url} with payload {payload}")
            r = requests.get(url, params=payload)

            results_raw = r.json()
            logging.info(f"Got results: {results_raw}")

            results = []
            for result_raw in results_raw.get('results', []):
                results.append({
                    'name': result_raw.get('name', ''),
                    'has_prime': result_raw.get('has_prime', False),
                    'price': result_raw.get('price_string', ''),
                    'stars': result_raw.get('stars', ''),
                    'total_reviews': result_raw.get('total_reviews', ''),
                    'url': result_raw.get('url', ''),

                })

            # Limit results to amount set in env var
            results = results[:int(self.get_tool_config("MAX_RESULTS"))]

            return results

        except Exception as error:
            print('An error occurred: %s' % error)
            return []

