# client_fastmcp.py
import asyncio
import json

from fastmcp import Client

# 配置服务器连接信息
config = {
    "mcpServers": {
        "hubbell": {
            "url": "http://localhost/sse",
            "transport": "sse"
        }
    }
}

async def main():
    client = Client(config)
    async with client:  # 使用异步上下文管理器管理连接
        # 调用工具
        tools = await client.list_tools()
        print(tools)
        for tool in tools:
            print('-' * 30)
            print(tool.model_dump_json())
        result = await client.call_tool("information_extract", {"question": "Find the hubbell equivalent of leviton 7090-PG. Find the details in leviton.com"})
        print(f"Result: {result}")

if __name__ == "__main__":
    asyncio.run(main())