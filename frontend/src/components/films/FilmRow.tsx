import * as React from 'react';
import { Link } from 'react-router';
import { connect } from 'react-redux';

import Store from '../../state/store';
import IFilm from '../../models/IFilm';
import DeleteCell from '../generic/DeleteCell';
import { ScreenSize } from '../../models/IDeviceInfo';
import { IDispatch } from '../../state/actions/ActionTypes';
import { deleteFilm, IActionProps } from '../../state/film/actions/DeleteFilmAction';

export type Props = {
    film: IFilm;
    page: number;
};

type ConnectedState = {
    screenSize: ScreenSize;
};

type ConnectedDispatch = {
    deleteFilm: (props: IActionProps) => void;
};

type CombinedProps = Props & ConnectedDispatch & ConnectedState;
class FilmRowComponent extends React.Component<CombinedProps> {
    public render() {
        const film = this.props.film;
        const onDelete = () => {
            this.props.deleteFilm({
                id: film.id,
                currentPage: this.props.page
            });
        };
        const full = this.props.screenSize > ScreenSize.small || undefined;
        return (
            <tr>
                <td className="align-middle"><img src={film.posterUrl} width="80px" /></td>
                <td className="align-middle"><Link to={'/film/' + film.id} title={film.title}>{film.title}</Link></td>
                {full && <td className="align-middle">{film.year}</td>}
                {full && <DeleteCell onDelete={onDelete} />}
            </tr>
        );
    }
}

const mapStateToProps = (state: Store.All): ConnectedState => ({
    screenSize: state.deviceInfo.screenSize
});

const mapDispatchToProps = (dispatch: IDispatch): ConnectedDispatch => ({
    deleteFilm: (props: IActionProps) => dispatch(deleteFilm(props))
});

const FilmRow: React.ComponentClass<Props> =
    connect(mapStateToProps, mapDispatchToProps)(FilmRowComponent);
export default FilmRow;