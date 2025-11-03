# Generated Workflow from UI - BAML Workflow

This is an AI-powered workflow using BAML (Boundary ML) to accomplish complex tasks through LLM function calling.

## Environment Setup

**IMPORTANT**: Before running this workflow, you must set your OpenAI API key in your environment:

```bash
export OPENAI_API_KEY='your-api-key'
```

This environment variable is required for the workflow to make API calls to OpenAI. Make sure to set it before running either the setup script or any manual steps below.

## Workflow Steps

1. **define_daily_objectives**: List the top priorities for both children's daily development, education, and enjoyment.
2. **establish_home_boundaries**: Establish routines for behavior management, limit-setting, and empathy development for both children.
3. **schedule_parent_self-care**: Schedule and commit to personal development, skill-building activities, and socialization for the stay-at-home mom, acknowledging her own needs.
4. **map_child_needs_to_time_slots**: Categorize and schedule time allocations for work, home chores, nap times, meals, and activities per day, taking into account both children's needs. (using output from define_daily_objectives)
5. **organize_childhood_activities**: Organize and schedule activities like art projects, storytelling, sing-alongs, and motor skill development for both children. (using output from map_child_needs_to_time_slots)
6. **schedule_meals_and_snacks**: Create a daily meal schedule for the children and make arrangements for meal prep, cooking, and clean-up. (using output from map_child_needs_to_time_slots)
7. **create_bedtime_routine**: Estimate and schedule the timing for wind-down activities, relaxation techniques, and sleep preparation to ensure a smooth bedtime for both children. (using output from schedule_meals_and_snacks)
8. **finalize_daily_schedule**: Visualize and commit to a daily schedule for the stay-at-home mom that meets all her responsibilities and her children's needs, including time slots for personal development and self-care. (using output from organize_childhood_activities, establish_home_boundaries, create_bedtime_routine, schedule_meals_and_snacks, schedule_parent_self-care)
9. **review_and_adjust_schedule**: Monitor and revise the schedule as required, ensuring it remains useful and beneficial for the well-being of all household members. (using output from finalize_daily_schedule)

## Running the Workflow

This workflow is self-contained and requires minimal setup:

1. Run the setup script which will create a virtual environment and install dependencies:
```bash
./run.sh
```

2. Or follow these manual steps:
   * Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

   * Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   * Generate BAML client code:
   ```bash
   baml-cli generate
   ```

   * Run the workflow:
   ```bash
   python main.py
   ```

## Input/Output

- The workflow accepts input as either plain text or JSON
- Each BAML function processes its input and produces structured output
- Results from all steps are collected in the final output
