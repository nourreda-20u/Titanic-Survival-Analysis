"""Execute the notebook in order and save actual text, table and image outputs."""
import ast
import base64
import contextlib
import io
import json
from pathlib import Path
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
os.chdir(ROOT)
path = ROOT / 'notebooks/titanic_analysis.ipynb'
notebook = json.loads(path.read_text())
namespace = {'__name__': '__main__'}
count = 0
for index, cell in enumerate(notebook['cells']):
    if cell['cell_type'] != 'code':
        continue
    count += 1
    outputs = []
    cell['execution_count'] = count
    stream = io.StringIO()
    def show(*args, **kwargs):
        for number in plt.get_fignums():
            figure = plt.figure(number)
            buffer = io.BytesIO()
            figure.savefig(buffer, format='png', bbox_inches='tight')
            outputs.append({'output_type': 'display_data', 'metadata': {}, 'data': {'image/png': base64.b64encode(buffer.getvalue()).decode()}})
        plt.close('all')
    plt.show = show
    tree = ast.parse(''.join(cell['source']))
    last = tree.body.pop() if tree.body and isinstance(tree.body[-1], ast.Expr) else None
    with contextlib.redirect_stdout(stream):
        exec(compile(tree, f'cell_{index}', 'exec'), namespace)
        if last is not None:
            value = eval(compile(ast.Expression(last.value), f'cell_{index}', 'eval'), namespace)
            if value is not None:
                data = {'text/plain': repr(value)}
                if isinstance(value, pd.DataFrame):
                    data['text/html'] = value.to_html()
                outputs.append({'output_type': 'execute_result', 'execution_count': count, 'metadata': {}, 'data': data})
    if stream.getvalue():
        outputs.insert(0, {'output_type': 'stream', 'name': 'stdout', 'text': stream.getvalue()})
    cell['outputs'] = outputs
path.write_text(json.dumps(notebook, indent=1))
print(f'Executed {count} code cells successfully.')
print('Prepared rows:', len(namespace['df_clean']))
print('Survivors:', int(namespace['df_clean']['Survived'].sum()))
print('Figures:', len(list((ROOT / 'outputs/figures').glob('*.png'))))
