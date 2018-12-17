import os
import yaml

global info_dict
generic_data = yaml.load(open('test/feature/config.yml'))


def before_all(contex):
    contex.url = generic_data['app']['url']
    contex.api_token = generic_data['app']['api_token']
    print '||||||||||||| BEFORE ALL |||||||||||||'


def before_feature(context, feature):
    if "try" in feature.tags:
        print '-----  Feature try tags -----'
    if 'Test' in feature.name:
        print '________FEATURE TEST________'


def before_scenario(context, scenario):
    if 'tag_scenario' in scenario.tags:
        print "//////----//// SCENARIOS TAGS /////------////"
    if 'Test':
        print '________SCENARIO TEST________'


def before_step(context, step):
    print ("STEP", step.name)
    print ("STEP KEYWORD", step.keyword)
    print ("STEP SATUS", step.status)
