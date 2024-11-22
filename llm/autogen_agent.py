from autogen import AutogenAgent


def initialize_agent():
    agent = AutogenAgent(config_path='config/autogen_config.yml')
    agent.register_tool('database_schema_tool', DatabaseSchemaTool())
    agent.register_tool('query_planner_tool', QueryPlannerTool())
    agent.register_tool('data_profiler_tool', DataProfilerTool())
    return agent
