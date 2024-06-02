
# Ponyhelper Extension for Stable Diffusion Web UI

## Overview

The Ponyhelper extension for Stable Diffusion Web UI is designed to assist users in creating prompts for the PonyXL model. This extension allows you to prepend dynamic scoring sequences to your prompts based on a configurable slider, helping with quality control using score tags.

## Features

- **Enable/Disable ScorePrompt**: Easily toggle the ScorePrompt feature on or off using a checkbox.
- **Score Level Slider**: Adjust the scoring sequence from 1 to 9 using a slider.
- **Dynamic Accordion Label**: The Accordion label updates based on the checkbox state, displaying "Active" or "Not Active".
- **Prefix and Negative Prefix Generation**: Automatically prepend score sequences to both positive and negative prompts based on the selected score level.

## Installation

To install the Ponyhelper extension, follow these steps:

1. Ensure you have the latest Automatic1111 stable-diffusion-webui version ≥ 1.93 installed.

2. Open the "Extensions" tab and navigate to the "Install from URL" section.

3. Paste the repository URL into the "URL for extension's git repository" field:

   ```
   https://github.com/DOGMANTC/sd-webui-ponyhelper.git
   ```

4. Press the Install button. Wait a few seconds for the extension to finish installing.

5. Restart the Web UI: Completely restart your Stable Diffusion Web UI to load the new extension.

## Usage

1. **Enable the Extension**: In the Stable Diffusion Web UI, navigate to the Ponyhelper extension.
2. **Configure the Slider**: Adjust the score level slider to your desired level.
3. **Generate Prompts**: The extension will automatically prepend the appropriate score sequence to your prompts.

### Example

- **Slider set to 6**:
  - Positive Prompt Prefix: `score_9, score_8_up, score_7_up, score_6_up, `
  - Negative Prompt Prefix: `score_5, score_4, score_3, score_2, score_1, `

- **Slider set to 2**:
  - Positive Prompt Prefix: `score_9, score_8_up, score_7_up, score_6_up, score_5_up, score_4_up, score_3_up, score_2_up, `
  - Negative Prompt Prefix: `score_1, `

- **Slider set to 8**:
  - Positive Prompt Prefix: `score_9, score_8_up, `
  - Negative Prompt Prefix: `score_7, score_6, score_5, score_4, score_3, score_2, score_1, `

## Development

### Prerequisites

- Python 3.x
- Gradio
- Stable Diffusion Web UI

### Code Structure

- **`ScorePromptScript` Class**: Main class implementing the ScorePrompt functionality.
- **UI Methods**: Methods to build the Gradio UI components.
- **Process Methods**: Methods to handle prompt modification based on user input.

### Adding New Features

1. Fork the repository.
2. Create a new branch for your feature.
3. Implement and test your feature.
4. Create a pull request with a detailed description of your changes.

## Contributing

We welcome contributions from the community. Please read our [contributing guidelines](CONTRIBUTING.md) for more information.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For issues, questions, or suggestions, please open an issue in this repository or contact us at [your-email@example.com](mailto:your-email@example.com).

---

Thank you for using Ponyhelper! Happy prompting!
