import Store from '../../store';
import globals from '../../utilities/globals';
import { invalidate } from './ForumTopicAction';
import { remove } from '../../utilities/Requestor';
import { IUnkownError } from '../../models/base/IError';
import { ThunkAction, IDispatch } from '../ActionTypes';
import ErrorAction, { handleError } from '../ErrorAction';

type DeleteThreadAction =
    { type: 'DELETING_FORUM_THREAD', id: number } |
    { type: 'DELETED_FORUM_THREAD', id: number } |
    { type: 'FAILED_DELETING_FORUM_THREAD', id: number };
export default DeleteThreadAction;
type Action = DeleteThreadAction | ErrorAction;

export interface IDeleteThreadProps {
    topic: number;
    thread: number;
    currentPage: number;
}

function deleting(id: number): Action {
    return { type: 'DELETING_FORUM_THREAD', id };
}

function deleted(id: number): Action {
    return { type: 'DELETED_FORUM_THREAD', id };
}

function failure(id: number): Action {
    return { type: 'FAILED_DELETING_FORUM_THREAD', id };
}

export function deleteForumThread(props: IDeleteThreadProps): ThunkAction<Action> {
    return (dispatch: IDispatch<Action>, getState: () => Store.All) => {
        const state = getState();
        dispatch(deleting(props.thread));
        return deleteThread(state.sealed.auth.token, props.thread).then((response: any) => {
            const action = dispatch(deleted(response.id));
            dispatch(invalidate({ id: props.topic, page: props.currentPage }));
            return action;
        }, (error: IUnkownError) => {
            dispatch(failure(props.thread));
            return dispatch(handleError(error));
        });
    };
}

function deleteThread(token: string, id: number): Promise<any> {
    return remove({ token, url: `${globals.apiUrl}/forum-thread-index/${id}/` });
}