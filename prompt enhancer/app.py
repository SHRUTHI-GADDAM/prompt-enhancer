import streamlit as st

st.set_page_config(
    page_title="Image Prompt Enhancer",
    page_icon="🎨",
    layout="wide"
)

st.title("🎨 AI Image Prompt Enhancer")

st.write(
    "Transform simple ideas into detailed prompts for AI image generation."
)

user_input = st.text_input(
    "Enter a simple prompt",
    placeholder="Example: big red building"
)

def generate_prompts(prompt):

    prompts = [
        {
            "title": "Photorealistic Version",
            "prompt": f"""
A massive red skyscraper made of polished crimson steel and reflective glass,
standing in the center of a futuristic city during golden hour. Warm cinematic
lighting reflects across nearby buildings while soft fog surrounds the lower streets.
Captured from a low-angle wide shot using a 24mm lens, ultra-detailed textures,
photorealistic architecture, dramatic shadows, realistic atmosphere, high dynamic range,
sharp focus, modern urban environment, cinematic composition.
""",
            "reason": """
- Adds realistic architectural materials and textures
- Improves atmosphere with cinematic lighting
- Includes camera angle and lens details
- Makes the image generation more precise
"""
        },

        {
            "title": "Cyberpunk Version",
            "prompt": f"""
A giant glowing red tower in a neon cyberpunk megacity at night, covered with holographic advertisements,
rain-soaked metallic surfaces, vibrant reflections, flying vehicles surrounding the skyline,
dark futuristic atmosphere, blue and red neon lighting, dramatic perspective shot,
captured with a cinematic anamorphic lens, highly detailed environment,
science-fiction aesthetic, volumetric lighting, dystopian mood.
""",
            "reason": """
- Introduces a futuristic cyberpunk style
- Enhances mood using neon lighting and rain
- Adds cinematic sci-fi composition
- Creates stronger visual storytelling
"""
        },

        {
            "title": "Fantasy Painting Version",
            "prompt": f"""
An enormous enchanted red castle built on a floating island above the clouds,
surrounded by glowing magical crystals and flying dragons. Soft sunset lighting,
dreamlike atmosphere, painterly textures, fantasy art style inspired by epic storybooks,
wide aerial composition, magical fog, vibrant colors, highly detailed environment,
watercolor and digital painting hybrid aesthetic.
""",
            "reason": """
- Converts the original idea into fantasy art
- Adds magical world-building elements
- Uses artistic style references
- Enhances visual creativity and uniqueness
"""
        }
    ]

    return prompts

if st.button("Generate Enhanced Prompts"):

    if user_input:

        prompts = generate_prompts(user_input)

        cols = st.columns(3)

        for col, item in zip(cols, prompts):

            with col:

                st.card = st.container()

                with st.card:

                    st.subheader(item["title"])

                    st.write(item["prompt"])

                    st.markdown("### Why this works")

                    st.write(item["reason"])

    else:

        st.warning("Please enter a prompt.")
