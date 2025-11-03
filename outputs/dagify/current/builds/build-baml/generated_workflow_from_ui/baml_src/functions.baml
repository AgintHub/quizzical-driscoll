function Process_create_bedtime_routine(schedule_meals_and_snacks_output: string) -> string {
  client DefaultOpenAI
  prompt #"
    Estimate and schedule the timing for wind-down activities, relaxation techniques, and sleep preparation to ensure a smooth bedtime for both children.

    Input:
    {{ schedule_meals_and_snacks_output }}

    Output Format:
    {{ ctx.output_format }} // Escaped curly braces for Jinja context
  "#
}

function Process_define_daily_objectives(input_payload: string) -> string {
  client DefaultOpenAI
  prompt #"
    List the top priorities for both children's daily development, education, and enjoyment.

    Input:
    {{ input_payload }}

    Output Format:
    {{ ctx.output_format }} // Escaped curly braces for Jinja context
  "#
}

function Process_establish_home_boundaries(input_payload: string) -> string {
  client DefaultOpenAI
  prompt #"
    Establish routines for behavior management, limit-setting, and empathy development for both children.

    Input:
    {{ input_payload }}

    Output Format:
    {{ ctx.output_format }} // Escaped curly braces for Jinja context
  "#
}

function Process_finalize_daily_schedule(organize_childhood_activities_output: string, establish_home_boundaries_output: string, create_bedtime_routine_output: string, schedule_meals_and_snacks_output: string, schedule_parent_self_care_output: string) -> string {
  client DefaultOpenAI
  prompt #"
    Visualize and commit to a daily schedule for the stay-at-home mom that meets all her responsibilities and her children's needs, including time slots for personal development and self-care.

    Input:
    {{ organize_childhood_activities_output }}
    {{ establish_home_boundaries_output }}
    {{ create_bedtime_routine_output }}
    {{ schedule_meals_and_snacks_output }}
    {{ schedule_parent_self_care_output }}

    Output Format:
    {{ ctx.output_format }} // Escaped curly braces for Jinja context
  "#
}

function Process_map_child_needs_to_time_slots(define_daily_objectives_output: string) -> string {
  client DefaultOpenAI
  prompt #"
    Categorize and schedule time allocations for work, home chores, nap times, meals, and activities per day, taking into account both children's needs.

    Input:
    {{ define_daily_objectives_output }}

    Output Format:
    {{ ctx.output_format }} // Escaped curly braces for Jinja context
  "#
}

function Process_organize_childhood_activities(map_child_needs_to_time_slots_output: string) -> string {
  client DefaultOpenAI
  prompt #"
    Organize and schedule activities like art projects, storytelling, sing-alongs, and motor skill development for both children.

    Input:
    {{ map_child_needs_to_time_slots_output }}

    Output Format:
    {{ ctx.output_format }} // Escaped curly braces for Jinja context
  "#
}

function Process_review_and_adjust_schedule(finalize_daily_schedule_output: string) -> string {
  client DefaultOpenAI
  prompt #"
    Monitor and revise the schedule as required, ensuring it remains useful and beneficial for the well-being of all household members.

    Input:
    {{ finalize_daily_schedule_output }}

    Output Format:
    {{ ctx.output_format }} // Escaped curly braces for Jinja context
  "#
}

function Process_schedule_meals_and_snacks(map_child_needs_to_time_slots_output: string) -> string {
  client DefaultOpenAI
  prompt #"
    Create a daily meal schedule for the children and make arrangements for meal prep, cooking, and clean-up.

    Input:
    {{ map_child_needs_to_time_slots_output }}

    Output Format:
    {{ ctx.output_format }} // Escaped curly braces for Jinja context
  "#
}

function Process_schedule_parent_self_care(input_payload: string) -> string {
  client DefaultOpenAI
  prompt #"
    Schedule and commit to personal development, skill-building activities, and socialization for the stay-at-home mom, acknowledging her own needs.

    Input:
    {{ input_payload }}

    Output Format:
    {{ ctx.output_format }} // Escaped curly braces for Jinja context
  "#
}
