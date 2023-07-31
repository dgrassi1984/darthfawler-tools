from abc import ABC
from superagi.tools.base_tool import BaseToolkit, BaseTool
from typing import Type, List
from search_on_amazon import SearchOnAmazonTool


class WebScrapingApiToolkit(BaseToolkit, ABC):
    name: str = "WebScarpingApi Toolkit"
    description: str = "Toolkit that enables access to webscrapingapi.com"

    def get_tools(self) -> List[BaseTool]:
        return [SearchOnAmazonTool()]

    def get_env_keys(self) -> List[str]:
        return ["API_KEY", "COUNTRY", "TLD", "MAX_RESULTS"]
    