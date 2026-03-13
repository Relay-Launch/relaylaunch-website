export interface ToggleChangeEvent extends CustomEvent {
  detail: {
    pressed: boolean;
    toggleId: string;
    syncGroup?: string;
  };
}
