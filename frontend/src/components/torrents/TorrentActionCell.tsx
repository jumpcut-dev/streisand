import * as React from 'react';
import { connect } from 'react-redux';
import { push } from 'react-router-redux';
import { Button, ButtonGroup } from 'reactstrap';

import globals from '../../utilities/globals';
import { ITorrent } from '../../models/ITorrent';
import { IDispatch } from '../../actions/ActionTypes';
import { deleteTorrent, IActionProps } from '../../actions/torrents/DeleteTorrentAction';

export type Props = {
    page?: number;
    torrent: ITorrent;
    includeDelete?: boolean;
    includeRelease?: boolean;
};

type ConnectedState = {};
type ConnectedDispatch = {
    editRelease: (id: number) => void;
    deleteItem: (props: IActionProps) => void;
};

type CombinedProps = Props & ConnectedDispatch & ConnectedState;
class TorrentActionCellComponent extends React.Component<CombinedProps> {
    public render() {
        const { torrent, page, includeDelete } = this.props;

        const includeRelease = this.props.includeRelease && torrent.release;
        const onEdit = () => this.props.editRelease(torrent.release || -404);
        const onDelete = () => {
            this.props.deleteItem({
                currentPage: page,
                id: torrent.id,
                release: torrent.release
            });
        };

        const downloadUrl = `${globals.baseUrl}${torrent.downloadUrl}`;
        return (
            <td>
                <div className="row justify-content-end no-gutters">
                    <ButtonGroup className="col-auto ml-auto" color="default" size="sm">
                        <a className="btn btn-secondary" href={downloadUrl} title="Download torrent file" role="button">
                            <i className="fas fa-arrow-down fa-lg" />
                        </a>
                        {includeRelease &&
                            <Button onClick={onEdit} title="View release">
                                <i className="fas fa-info-circle fa-lg" />
                            </Button>
                        }
                        {includeDelete &&
                            <Button color="danger" onClick={onDelete} title="Delete torrent">
                                <i className="fas fa-trash-alt fa-lg" />
                            </Button>
                        }
                    </ButtonGroup>
                </div>
            </td>
        );
    }
}
const mapDispatchToProps = (dispatch: IDispatch): ConnectedDispatch => ({
    editRelease: (id: number) => dispatch(push(`/release/${id}`)),
    deleteItem: (props: IActionProps) => dispatch(deleteTorrent(props))
});

const TorrentActionCell: React.ComponentClass<Props> =
    connect(undefined, mapDispatchToProps)(TorrentActionCellComponent);
export default TorrentActionCell;