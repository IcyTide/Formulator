import gradio as gr


class TopComponent:
    def __init__(self):
        with gr.Row():
            with gr.Column():
                with gr.Row():
                    self.upload_log = gr.UploadButton("上传JCL")
                    self.upload_json = gr.UploadButton("上传JSON")
                self.copy_json = gr.Textbox(label="复制JSON", show_copy_button=True, max_lines=2)

            with gr.Column():
                self.player_select = gr.Dropdown(label="选择角色", visible=False)
                self.target_select = gr.Dropdown(label="选择目标", visible=False)
