
import Action from './actions';
import { INewsStore } from './store';
import { combineReducers } from '../reducers/helpers';

function latest(state: number | null = null, action: Action): number | null {
    switch (action.type) {
        case 'RECEIVED_NEWS_POST':
            if (action.props.data.posts.length) {
                return action.props.data.posts[0].id;
            }
            return state;
        default:
            return state;
    }
}

function loading(state: boolean = false, action: Action): boolean {
    switch (action.type) {
        case 'REQUEST_NEWS_POST':
            return true;
        case 'FAILED_NEWS_POST':
        case 'RECEIVED_NEWS_POST':
            return false;
        default:
            return state;
    }
}

export default combineReducers<INewsStore>({ latest, loading });