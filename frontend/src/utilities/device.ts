import { ScreenSize } from '../models/IDeviceInfo';

export function getScreenSize(): ScreenSize {
    const width = window.innerWidth;
    if (width < 576) { return ScreenSize.extraSmall; }
    if (width < 768) { return ScreenSize.small; }
    if (width < 992) { return ScreenSize.medium; }
    if (width < 1200) { return ScreenSize.large; }
    return ScreenSize.extraLarge;
}
