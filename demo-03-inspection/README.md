# Demo 03: Data inspection

## Metadata

Run `f3d ../assets/eta_asm.stp`.
Explain that it's possible to inspect some details of the model. Press `M`.
Press `SHIFT+H` to show the scene hierarchy. Disable some parts.

## Scivis

Run `f3d ../assets/skull.vti`.
Explain that it's a scan of a human skull.
A color is mapped on each voxel value as shown on the color bar.
After a quick inspection, it's clear that it's not properly oriented and that low values (black) are mostly noise.

Run `f3d ../assets/skull.vti --coloring-range=30,255 --up=z`
