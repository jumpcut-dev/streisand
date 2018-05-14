import Store from '../../../store';
import globals from '../../../utilities/globals';
import { transformPostOnly } from '../transforms';
import { patch } from '../../../utilities/Requestor';
import { IUnkownError } from '../../../models/base/IError';
import { ThunkAction, IDispatch } from '../../ActionTypes';
import ErrorAction, { handleError } from '../../ErrorAction';
import { IForumPostResponse, IForumPost } from '../../../models/forums/IForumPost';

type UpdatePostAction =
    { type: 'UPDATING_FORUM_POST', id: number, content: string } |
    { type: 'UPDATED_FORUM_POST', post: IForumPost } |
    { type: 'FAILED_UPDATING_FORUM_POST', id: number };
export default UpdatePostAction;
type Action = UpdatePostAction | ErrorAction;

function updating(id: number, content: string): Action {
    return { type: 'UPDATING_FORUM_POST', id, content };
}

function updated(response: IForumPostResponse): Action {
    return {
        type: 'UPDATED_FORUM_POST',
        post: transformPostOnly(response)
    };
}

function failure(id: number): Action {
    return { type: 'FAILED_UPDATING_FORUM_POST', id };
}

export function updatePost(id: number, content: string): ThunkAction<Action> {
    return (dispatch: IDispatch<Action>, getState: () => Store.All) => {
        const state = getState();
        dispatch(updating(id, content));
        return update(state.sealed.auth.token, id, content).then((response: IForumPostResponse) => {
            return dispatch(updated(response));
        }, (error: IUnkownError) => {
            dispatch(failure(id));
            return dispatch(handleError(error));
        });
    };
}

function update(token: string, id: number, content: string): Promise<IForumPostResponse> {
    const data = { body: content };
    return patch({ token, url: `${globals.apiUrl}/forum-posts/${id}/`, data });
}