
# Generate parser
antlr4 -Dlanguage=Python3 -visitor app/agent_grammer/parser/ai_environment.g4

# Check Template Definitions
antlr4-parse app/agent_grammer/parser/ai_environment.g4 ai_envDef template-definitions/agentmicroservice.a4
