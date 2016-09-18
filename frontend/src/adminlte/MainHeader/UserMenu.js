import React from "react";
import classNames from "classnames";


class UserMenu extends React.Component {
    render() {
        const {actions, adminlte} = this.props;
        const userPanel = adminlte.getIn(["mainHeader", "userPanel"]);
        const staticRoot = window.django.urls.staticRoot;

        const classes = classNames({
            "dropdown": true,
            "user": true,
            "user-menu": true,
            "open": ! userPanel.get("collapsed")
        });

        return (
            <li className={classes}>
                <a
                    onClick={actions.mainHeaderUserMenuToggle}
                    className="cursor-pointer dropdown-toggle"
                >
                    <img
                        src={`${staticRoot}adminlte/img/user2-160x160.jpg`}
                        className="user-image" alt="User Image"
                    />
                    <span className="hidden-xs">{window.django.user.full_name}</span>
                </a>

                <ul className="dropdown-menu">
                    <li className="user-header">
                        <img src={`${staticRoot}adminlte/img/user2-160x160.jpg`}
                            className="img-circle" alt="User Image" />

                        <p>
                            {window.django.user.full_name}
                            <small>Last Login {window.django.user.last_login}</small>
                        </p>
                    </li>

            

                    <li className="user-footer">
                

                        <div className="pull-right">
                            <a href={window.django.urls.logout}
                            className="btn btn-default btn-flat">Sign out</a>
                        </div>
                    </li>
                </ul>
            </li>
        );
    }
}

export default UserMenu;
