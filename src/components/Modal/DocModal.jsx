import React from 'react';
import { Modal } from 'antd';

import DocEditForm from "../Form/DocEditForm";
import './DocModal.css'

const DocModal = (props) => (
      <Modal
        className="doc-modal"
        title="Edit Document"
        visible={props.visible}
        onOk={props.hideModal}
        onCancel={props.hideModal}
        cancelText="Close"
      >
        <DocEditForm/>
      </Modal>
)

export default DocModal
