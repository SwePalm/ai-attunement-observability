import os

def load_prompt_template(filepath):
    """
    Reads the content of the prompt template file into a single string.
    """
    if not os.path.exists(filepath):
        print(f"Error: Prompt template file not found at '{filepath}'")
        return None
    
    try:
        with open(filepath, 'r') as file:
            template = file.read()
            # print(f"Successfully loaded prompt template from {filepath}.")
            return template
    except Exception as e:
        print(f"An unexpected error occurred during template file loading: {e}")
        return None
    
    
def get_explore_question_prompt(theme = None, prompt_path="prompts/question_prompt.txt"):    

    if theme is None:
        print(f"Need to provide theme")
        return None

    question_prompt = load_prompt_template(prompt_path)

    final_question_prompt = str(question_prompt).format(
        theme_name=theme 
    )

    return final_question_prompt
    
    
def get_theme_exploration_prompt(theme=None, theme_question = None, prompt_path="prompts/theme_exploration_prompt.txt"):    

    if theme is None or theme_question is None:
        print(f"Need to provide theme and theme question.")
        return None
    
    theme_exploration_prompt = load_prompt_template(prompt_path)
    #print(theme_exploration_prompt)

    final_theme_exploration_prompt = str(theme_exploration_prompt).format(
        theme_title=theme, 
        theme_question=theme_question
    )

    return final_theme_exploration_prompt


def get_pestle_analysis_prompt(theme_exploration_text = None, prompt_path="prompts/pestle_prompt.txt"):    

    if theme_exploration_text is None:
        print(f"Need to provide theme exploration text")
        return None

    pestle_prompt = load_prompt_template(prompt_path)

    final_pestle_prompt = str(pestle_prompt).format(
        theme_exploration_response=theme_exploration_text 
    )

    return final_pestle_prompt


def get_forces_feelings_prompt(theme_exploration_text = None, pestle_analysis_text = None, prompt_path="prompts/forces_feelings_prompt.txt"):    

    if theme_exploration_text is None or pestle_analysis_text is None:
        print(f"Need to provide theme exploration text and pestle analysis text")
        return None

    ff_prompt = load_prompt_template(prompt_path)

    final_ff_prompt = str(ff_prompt).format(
        theme_exploration_response=theme_exploration_text,
        pestle_response=pestle_analysis_text 
    )

    return final_ff_prompt


def get_scenario_prompt(theme_exploration_text = None, pestle_analysis_text = None, forces_feelings_text = None,prompt_path="prompts/scenarios_prompt.txt"):    

    if theme_exploration_text is None or pestle_analysis_text is None or forces_feelings_text is None:
        print(f"Need to provide theme exploration text, pestle analysis text and forces feelings text")
        return None

    scenario_prompt = load_prompt_template(prompt_path)

    final_scenario_prompt = str(scenario_prompt).format(
        theme_exploration_response=theme_exploration_text,
        pestle_response=pestle_analysis_text,
        forces_feelings_response=forces_feelings_text
    )
    return final_scenario_prompt


def get_jester_prompt(scenario_text = None,prompt_path="prompts/jester_prompt.txt"):    

    if scenario_text is None:
        print(f"Need to provide scenario to reflect on.")
        return None

    jester_prompt = load_prompt_template(prompt_path)

    final_jester_prompt = str(jester_prompt).format(
        scenario_text=scenario_text
    )
    return final_jester_prompt


def get_framework_prompt(all_themes_info = None,prompt_path="prompts/framework_prompt.txt"):    

    if all_themes_info is None:
        print(f"Need to provide theme information to create framework")
        return None

    framework_prompt = load_prompt_template(prompt_path)

    final_framework_prompt = str(framework_prompt).format(
        data_to_framework=all_themes_info,
    )
    return final_framework_prompt


def get_waves_list_prompt(the_framework = None,prompt_path="prompts/waves_list_prompt.txt"):    

    if the_framework is None:
        print(f"Need to provide the framework to extract the waves")
        return None

    waves_list_prompt = load_prompt_template(prompt_path)

    final_waves_list_prompt = str(waves_list_prompt).format(
        the_framework=the_framework,
    )
    return final_waves_list_prompt


def get_create_indicators_prompt(wave_info = None,prompt_path="prompts/create_indicators_prompt.txt"):    

    if wave_info is None:
        print(f"Need to provide wave information")
        return None

    indicators_prompt = load_prompt_template(prompt_path)

    final_indicators_prompt = str(indicators_prompt).format(
        current_wave = wave_info,
    )
    return final_indicators_prompt


def get_update_timeline_prompt(all_signals = None, draft_framework = None, prompt_path="prompts/update_timeline_prompt.txt"):    

    if all_signals is None or draft_framework is None:
        print(f"Need to provide signals and framework.")
        return None

    timeline_prompt = load_prompt_template(prompt_path)

    final_timeline_prompt = str(timeline_prompt).format(
        all_signals=all_signals,
        draft_framework=draft_framework 
    )
    return final_timeline_prompt


def get_timeline_specifics_prompt(timeline_table = None, all_signals = None, draft_framework = None, prompt_path="prompts/timeline_specifics_prompt.txt"):    

    if timeline_table is None or all_signals is None or draft_framework is None:
        print(f"Need to provide timeline table, signals and framework.")
        return None

    timeline_specifics_prompt = load_prompt_template(prompt_path)

    final_timeline_specifics_prompt = str(timeline_specifics_prompt).format(
        timeline_table=timeline_table,
        all_signals=all_signals,
        draft_framework=draft_framework 
    )
    return final_timeline_specifics_prompt


def get_update_framework_prompt(draft_framework = None, timeline_table = None, specifics = None, prompt_path="prompts/update_framework_prompt.txt"):    

    if timeline_table is None or specifics is None or draft_framework is None:
        print(f"Need to provide timeline table, signals and framework.")
        return None

    timeline_specifics_prompt = load_prompt_template(prompt_path)

    final_timeline_specifics_prompt = str(timeline_specifics_prompt).format(
        draft_framework=draft_framework,
        timeline_table=timeline_table,
        specifics=specifics
    )
    return final_timeline_specifics_prompt


def get_report_prompt(final_framework = None,prompt_path="prompts/report_prompt.txt"):    

    if final_framework is None:
        print(f"Need to provide the framework to this prompt")
        return None

    report_prompt = load_prompt_template(prompt_path)

    final_report_prompt = str(report_prompt).format(
        final_framework=final_framework,
    )
    return final_report_prompt


def get_meta_analysis_prompt(frameworks = None, prompt_path="prompts/meta_analysis_prompt.txt"):
    
    if frameworks is None:
        print(f"Need to provide frameworks to this prompt")
        return None

    report_prompt = load_prompt_template(prompt_path)

    final_meta_prompt = str(report_prompt).format(
        frameworks=frameworks,
    )
    return final_meta_prompt