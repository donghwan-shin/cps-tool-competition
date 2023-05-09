#!/usr/bin/env python

import argparse
import subprocess



# 创建参数解析器
parser = argparse.ArgumentParser(description='Run competition script with specified parameters.')
parser.add_argument('--time-budget', type=int, default=1800, help='Time budget in seconds (default: 1800)')
parser.add_argument('--executor', type=str, default='beamng', help='Executor to use (default: beamng)')
parser.add_argument('--map-size', type=int, default=200, help='Map size (default: 200)')
parser.add_argument('--module-name', type=str, default='sample_test_generators.GA_test_generator', help='Module name '
                                                                                                        '(default: '
                                                                                                        'sample_test_generators.GA_test_generator)')
parser.add_argument('--class-name', type=str, default='GATestGenerator', help='Class name (default: GATestGenerator)')

# 解析命令行参数
args = parser.parse_args()

# 构造命令行参数
cmd_args = ['python', 'competition.py']
cmd_args += ['--time-budget', str(args.time_budget)]
cmd_args += ['--executor', args.executor]
cmd_args += ['--map-size', str(args.map_size)]
cmd_args += ['--module-name', args.module_name]
cmd_args += ['--class-name', args.class_name]

# 执行命令行
subprocess.run(cmd_args)
