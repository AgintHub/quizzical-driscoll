import asyncio
import os
import json
from typing import Any, Dict

class BamlObjectEncoder(json.JSONEncoder):
    """Custom JSON encoder for BAML objects."""
    def default(self, obj):
        # Convert BAML objects to dictionaries
        if hasattr(obj, "__dict__"):
            return obj.__dict__
        # Handle other special types if needed
        elif hasattr(obj, "model_dump"):
            # Support for Pydantic models
            return obj.model_dump()
        # Let the base encoder handle standard types
        return super().default(obj)

def serialize_results(result_obj):
    """Convert potentially complex objects to JSON-serializable format."""
    if hasattr(result_obj, "__dict__"):
        return {k: serialize_results(v) for k, v in result_obj.__dict__.items() if not k.startswith("_")}
    elif isinstance(result_obj, dict):
        return {k: serialize_results(v) for k, v in result_obj.items()}
    elif isinstance(result_obj, list):
        return [serialize_results(item) for item in result_obj]
    elif hasattr(result_obj, "model_dump"):
        return serialize_results(result_obj.model_dump())
    else:
        return result_obj

if not os.getenv("OPENAI_API_KEY"):
    print("Error: OPENAI_API_KEY environment variable is not set.")
    print("Please set it with: export OPENAI_API_KEY='your-api-key'")
    print("This key is required for the BAML workflow to make API calls to OpenAI.")
    exit(1)

try:
    from baml_client import b
except ImportError:
    print("Warning: baml_client not found. Please run 'baml-cli generate' in the project root after baml_src is populated.")
    b = None

results_store: Dict[str, Any] = {}

async def run_define_daily_objectives(initial_input: Any) -> Any:
    print(f"Executing: define_daily_objectives...")
    if not b:
        print(f"Skipping Process_define_daily_objectives as baml_client is not available.")
        return None
    try:
        result = await b.Process_define_daily_objectives(input_payload=initial_input)
        # Convert result to a serializable format
        serializable_result = serialize_results(result)
        print(f"define_daily_objectives Result: {result}")
        results_store["define_daily_objectives"] = serializable_result
        return result
    except Exception as e:
        print(f"Error executing Process_define_daily_objectives: {e}")
        results_store["define_daily_objectives"] = f"Error: {e}"
        return None

async def run_establish_home_boundaries(initial_input: Any) -> Any:
    print(f"Executing: establish_home_boundaries...")
    if not b:
        print(f"Skipping Process_establish_home_boundaries as baml_client is not available.")
        return None
    try:
        result = await b.Process_establish_home_boundaries(input_payload=initial_input)
        # Convert result to a serializable format
        serializable_result = serialize_results(result)
        print(f"establish_home_boundaries Result: {result}")
        results_store["establish_home_boundaries"] = serializable_result
        return result
    except Exception as e:
        print(f"Error executing Process_establish_home_boundaries: {e}")
        results_store["establish_home_boundaries"] = f"Error: {e}"
        return None

async def run_schedule_parent_self_care(initial_input: Any) -> Any:
    print(f"Executing: schedule_parent_self-care...")
    if not b:
        print(f"Skipping Process_schedule_parent_self_care as baml_client is not available.")
        return None
    try:
        result = await b.Process_schedule_parent_self_care(input_payload=initial_input)
        # Convert result to a serializable format
        serializable_result = serialize_results(result)
        print(f"schedule_parent_self-care Result: {result}")
        results_store["schedule_parent_self-care"] = serializable_result
        return result
    except Exception as e:
        print(f"Error executing Process_schedule_parent_self_care: {e}")
        results_store["schedule_parent_self-care"] = f"Error: {e}"
        return None

async def run_map_child_needs_to_time_slots(define_daily_objectives_output: Any) -> Any:
    print(f"Executing: map_child_needs_to_time_slots...")
    if not b:
        print(f"Skipping Process_map_child_needs_to_time_slots as baml_client is not available.")
        return None
    try:
        result = await b.Process_map_child_needs_to_time_slots(define_daily_objectives_output=define_daily_objectives_output)
        # Convert result to a serializable format
        serializable_result = serialize_results(result)
        print(f"map_child_needs_to_time_slots Result: {result}")
        results_store["map_child_needs_to_time_slots"] = serializable_result
        return result
    except Exception as e:
        print(f"Error executing Process_map_child_needs_to_time_slots: {e}")
        results_store["map_child_needs_to_time_slots"] = f"Error: {e}"
        return None

async def run_organize_childhood_activities(map_child_needs_to_time_slots_output: Any) -> Any:
    print(f"Executing: organize_childhood_activities...")
    if not b:
        print(f"Skipping Process_organize_childhood_activities as baml_client is not available.")
        return None
    try:
        result = await b.Process_organize_childhood_activities(map_child_needs_to_time_slots_output=map_child_needs_to_time_slots_output)
        # Convert result to a serializable format
        serializable_result = serialize_results(result)
        print(f"organize_childhood_activities Result: {result}")
        results_store["organize_childhood_activities"] = serializable_result
        return result
    except Exception as e:
        print(f"Error executing Process_organize_childhood_activities: {e}")
        results_store["organize_childhood_activities"] = f"Error: {e}"
        return None

async def run_schedule_meals_and_snacks(map_child_needs_to_time_slots_output: Any) -> Any:
    print(f"Executing: schedule_meals_and_snacks...")
    if not b:
        print(f"Skipping Process_schedule_meals_and_snacks as baml_client is not available.")
        return None
    try:
        result = await b.Process_schedule_meals_and_snacks(map_child_needs_to_time_slots_output=map_child_needs_to_time_slots_output)
        # Convert result to a serializable format
        serializable_result = serialize_results(result)
        print(f"schedule_meals_and_snacks Result: {result}")
        results_store["schedule_meals_and_snacks"] = serializable_result
        return result
    except Exception as e:
        print(f"Error executing Process_schedule_meals_and_snacks: {e}")
        results_store["schedule_meals_and_snacks"] = f"Error: {e}"
        return None

async def run_create_bedtime_routine(schedule_meals_and_snacks_output: Any) -> Any:
    print(f"Executing: create_bedtime_routine...")
    if not b:
        print(f"Skipping Process_create_bedtime_routine as baml_client is not available.")
        return None
    try:
        result = await b.Process_create_bedtime_routine(schedule_meals_and_snacks_output=schedule_meals_and_snacks_output)
        # Convert result to a serializable format
        serializable_result = serialize_results(result)
        print(f"create_bedtime_routine Result: {result}")
        results_store["create_bedtime_routine"] = serializable_result
        return result
    except Exception as e:
        print(f"Error executing Process_create_bedtime_routine: {e}")
        results_store["create_bedtime_routine"] = f"Error: {e}"
        return None

async def run_finalize_daily_schedule(create_bedtime_routine_output: Any, establish_home_boundaries_output: Any, organize_childhood_activities_output: Any, schedule_meals_and_snacks_output: Any, schedule_parent_self_care_output: Any) -> Any:
    print(f"Executing: finalize_daily_schedule...")
    if not b:
        print(f"Skipping Process_finalize_daily_schedule as baml_client is not available.")
        return None
    try:
        result = await b.Process_finalize_daily_schedule(create_bedtime_routine_output=create_bedtime_routine_output, establish_home_boundaries_output=establish_home_boundaries_output, organize_childhood_activities_output=organize_childhood_activities_output, schedule_meals_and_snacks_output=schedule_meals_and_snacks_output, schedule_parent_self_care_output=schedule_parent_self_care_output)
        # Convert result to a serializable format
        serializable_result = serialize_results(result)
        print(f"finalize_daily_schedule Result: {result}")
        results_store["finalize_daily_schedule"] = serializable_result
        return result
    except Exception as e:
        print(f"Error executing Process_finalize_daily_schedule: {e}")
        results_store["finalize_daily_schedule"] = f"Error: {e}"
        return None

async def run_review_and_adjust_schedule(finalize_daily_schedule_output: Any) -> Any:
    print(f"Executing: review_and_adjust_schedule...")
    if not b:
        print(f"Skipping Process_review_and_adjust_schedule as baml_client is not available.")
        return None
    try:
        result = await b.Process_review_and_adjust_schedule(finalize_daily_schedule_output=finalize_daily_schedule_output)
        # Convert result to a serializable format
        serializable_result = serialize_results(result)
        print(f"review_and_adjust_schedule Result: {result}")
        results_store["review_and_adjust_schedule"] = serializable_result
        return result
    except Exception as e:
        print(f"Error executing Process_review_and_adjust_schedule: {e}")
        results_store["review_and_adjust_schedule"] = f"Error: {e}"
        return None

async def main(initial_workflow_input: Any):
    print("Starting BAML DAG workflow...")
    # --- Level 0 ---
    level_0_tasks = []
    level_0_tasks.append(run_define_daily_objectives(initial_workflow_input))
    level_0_tasks.append(run_establish_home_boundaries(initial_workflow_input))
    level_0_tasks.append(run_schedule_parent_self_care(initial_workflow_input))
    await asyncio.gather(*level_0_tasks)
    # --- Level 1 ---
    level_1_tasks = []
    level_1_tasks.append(run_map_child_needs_to_time_slots(results_store['define_daily_objectives']))
    await asyncio.gather(*level_1_tasks)
    # --- Level 2 ---
    level_2_tasks = []
    level_2_tasks.append(run_organize_childhood_activities(results_store['map_child_needs_to_time_slots']))
    level_2_tasks.append(run_schedule_meals_and_snacks(results_store['map_child_needs_to_time_slots']))
    await asyncio.gather(*level_2_tasks)
    # --- Level 3 ---
    level_3_tasks = []
    level_3_tasks.append(run_create_bedtime_routine(results_store['schedule_meals_and_snacks']))
    await asyncio.gather(*level_3_tasks)
    # --- Level 4 ---
    level_4_tasks = []
    level_4_tasks.append(run_finalize_daily_schedule(results_store['create_bedtime_routine'], results_store['establish_home_boundaries'], results_store['organize_childhood_activities'], results_store['schedule_meals_and_snacks'], results_store['schedule_parent_self-care']))
    await asyncio.gather(*level_4_tasks)
    # --- Level 5 ---
    level_5_tasks = []
    level_5_tasks.append(run_review_and_adjust_schedule(results_store['finalize_daily_schedule']))
    await asyncio.gather(*level_5_tasks)

    print("\nWorkflow execution finished.")
    print("Final results_store:")
    # Use the custom JSON encoder to safely serialize BAML objects
    try:
        print(json.dumps(results_store, indent=2, cls=BamlObjectEncoder))
    except TypeError as e:
        print(f"Error serializing results: {e}")
        print("Simplified results:")
        for k, v in results_store.items():
            print(f"  {k}: {type(v).__name__}")
    return results_store

if __name__ == "__main__":
    print("Enter initial input for the workflow (JSON string or plain text):")
    cli_input_str = input()
    try:
        initial_input_data = json.loads(cli_input_str)
    except json.JSONDecodeError:
        initial_input_data = cli_input_str
    asyncio.run(main(initial_input_data))