# -*- coding: utf-8 -*-
# pylint: disable=manifest-required-author, manifest-deprecated-key
{
    'name': 'Open e-Obs SLAM Configuration',
    'version': '0.1',
    'category': 'Clinical',
    'license': 'AGPL-3',
    'summary': '',
    'description': """
    A configuration module for South London & Maudsley NHS Foundation Trust
    """,
    'author': 'Neova Health',
    'website': 'http://www.neovahealth.co.uk/',
    'depends': [
        'nh_eobs_mobile',
        'nh_eobs_mental_health',
        'nh_neurological',
        # 'nh_food_and_fluid',
        'nh_weight',
        'web_graph',
    ],
    'data': ['security/ir.model.access.csv',
             'data/slam_master_data.xml',
             'views/mobile_template.xml',
             'views/wardboard.xml',
             'views/web_graph_view.xml',
             'data/slam_hospital_data.xml',
             'data/slam_1_ann_moss_way_wards.xml',
             'data/slam_27_inglemere_road_wards.xml',
             'data/slam_158_foxley_lane_wards.xml',
             'data/slam_bethlem_royal_wards.xml',
             'data/slam_lambeth_hospital_wards.xml',
             'data/slam_landor_road_wards.xml',
             'data/slam_lewisham_hospital_wards.xml',
             'data/slam_maudsley_hospital_wards.xml',
             'data/slam_n_a_wards.xml'
             ],
    'demo': [],
    'qweb': ['static/src/xml/slam.xml'],
    'css': [],
    'application': True,
    'installable': True,
    'active': False,
}
