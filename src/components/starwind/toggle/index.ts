import Toggle, { toggle } from "./Toggle.astro";
import type { ToggleChangeEvent } from "./ToggleTypes";

const ToggleVariants = { toggle };

export { Toggle, type ToggleChangeEvent, ToggleVariants };

export default Toggle;
