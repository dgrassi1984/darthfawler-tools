from abc import ABC
from superagi.tools.base_tool import BaseToolkit, BaseTool
from typing import Type, List
from search_on_amazon import SearchOnAmazonTool


class WebScrapingSpiToolkit(BaseToolkit, ABC):
    name: str = "Greetings Toolkit"
    description: str = "Greetings Tool kit contains all tools related to Greetings"

    def get_tools(self) -> List[BaseTool]:
        return [SearchOnAmazonTool()]

    def get_env_keys(self) -> List[str]:
        return ["API_KEY"]