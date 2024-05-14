import gradio as gr


class TopComponent:
    def __init__(self):
        with gr.Row():
            self.upload_log = gr.UploadButton("上传JCL")
            with gr.Column():
                self.upload_json = gr.UploadButton("上传JSON")
                self.save_json = gr.DownloadButton("保存JSON", visible=False)
            with gr.Column(scale=2):
                self.player_select = gr.Dropdown(label="选择角色", visible=False)
                self.target_select = gr.Dropdown(label="选择目标", visible=False)
