import os
import time
from pathlib import Path
from typing import Any

import f3d

TEST_DATA_DIR = Path(__file__).parent.parent / "assets"


def main():
    model_path = TEST_DATA_DIR / "bristleback_dota_fan-art.glb"
    options: dict[str, Any] = {
        "scene.up_direction": "+Y",
        "render.effect.tone_mapping": True,
        "scene.animation.autoplay": True,
        "render.effect.antialiasing.mode": "ssaa",
    }
    anim_fps = 30

    try:
        rows, cols = os.get_terminal_size()
    except OSError:
        rows, cols = 40, 20

    # setup offscreen engine
    engine = f3d.Engine.create(offscreen=True)
    engine.options.update(options)
    engine.scene.add(model_path)
    engine.window.size = rows, cols * 2

    [start_time, end_time] = engine.scene.animation_time_range()
    anim_duration = end_time - start_time

    engine.window.camera.zoom(1.2)

    # loop to move the camera and render frames
    for t in realtime_animation_timesteps(anim_fps, anim_duration):
        engine.scene.load_animation_time(t)
        image = engine.window.render_to_image(no_background=True)
        print(image.to_terminal_text(), end="")
    print()


def realtime_animation_timesteps(fps: float, duration: float):
    """Generate times at `fps`frame/s accounting for actual frame computation time."""
    target_frame_duration = 1.0 / fps
    start_time = time.time()
    end_time = start_time + duration
    while time.time() < end_time:
        frame_start_time = time.time()

        yield frame_start_time - start_time

        actual_frame_duration = time.time() - frame_start_time
        time.sleep(max(target_frame_duration - actual_frame_duration, 0))


if __name__ == "__main__":
    main()
