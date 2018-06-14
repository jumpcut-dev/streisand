import { put } from 'redux-saga/effects';

import globals from '../../utilities/globals';
import { post } from '../../utilities/Requestor';
import IRelease, { IReleaseUpdate } from '../../models/IRelease';
import { generateAuthFetch, generateSage } from '../sagas/generators';

export interface IActionProps {
    finished?: (id: number) => void;
    data: IReleaseUpdate;
}

export type RequestNewRelease = { type: 'REQUEST_NEW_RELEASE', props: IActionProps };
export type ReceivedNewRelease = { type: 'RECEIVED_NEW_RELEASE', release: IRelease };
export type FailedNewRelease = { type: 'FAILED_NEW_RELEASE', props: IActionProps };

type CreateReleaseAction = RequestNewRelease | ReceivedNewRelease | FailedNewRelease;
export default CreateReleaseAction;
type Action = CreateReleaseAction;

function* received(release: IRelease, props: IActionProps) {
    if (props.finished) {
        props.finished(release.id);
    }
    yield put<Action>({ type: 'RECEIVED_NEW_RELEASE', release });
}

function failure(props: IActionProps): Action {
    return { type: 'FAILED_NEW_RELEASE', props };
}

export function createRelease(props: IActionProps): Action {
    return { type: 'REQUEST_NEW_RELEASE', props };
}

const errorPrefix = 'Creating a new torrent failed';
const fetch = generateAuthFetch({ errorPrefix, request, received, failure });
export const createReleaseSaga = generateSage<RequestNewRelease>('REQUEST_NEW_RELEASE', fetch);

function request(token: string, props: IActionProps): Promise<IRelease> {
    return post({ token, data: props.data, url: `${globals.apiUrl}/releases/` });
}