import React from 'react';
import { Form, Row, Col, Input, Button, Icon, DatePicker, Select, Affix} from 'antd';
import moment from 'moment';
import $ from 'jquery';

import './DocEditForm.css'

const { MonthPicker, RangePicker } = DatePicker;
const { Option } = Select;

const dateFormat = 'YYYY/MM/DD';
const monthFormat = 'YYYY/MM';

const formItemLayout = {
  labelCol: {
    xs: { span: 24 },
    sm: { span: 8 },
  },
  wrapperCol: {
    xs: { span: 24 },
    sm: { span: 16 },
  },
};

class BasicForm extends React.Component {
  state = {
    expand: false,
  };

  handleReset = () => {
    this.props.form.resetFields();
  };

  toggle = () => {
    const { expand } = this.state;
    this.setState({ expand: !expand });
  };

  handleSubmit = e => {
    e.preventDefault();
    this.props.form.validateFields((err, values) => {


      if (!err) {
        console.log('Received values of form: ', values);
      }

    });
  };

  render() {
    let docVisible = this.props.docVisible;
    let formVisible = this.props.formVisible;

    const { getFieldDecorator } = this.props.form;

    return (
      <Row gutter={10} style={{marginTop: 10}}>
          {
            docVisible && formVisible &&
            <Col span={12}>
                <Affix offsetTop={80}>
                  <iframe className="preview-doc" src="http://localhost:8001/static/doc116.html"></iframe>
                </Affix>
            </Col>
          }
          {
            docVisible && !formVisible &&
            <Col span={24}>
                <iframe className="preview-doc vh-100" height="100%" src="http://localhost:8001/static/doc116.html"></iframe>
            </Col>
          }
          {
            formVisible &&
              <Col span={12}>
                  <Form {...formItemLayout} onSubmit={this.handleSubmit} className="doc-edit-form">
                    <Form.Item label={'Document Title'}>
                      {getFieldDecorator('document', {
                        rules: [
                          {
                            required: true,
                            message: 'Input something!',
                          },
                        ],
                      })(<Input  />)}
                    </Form.Item>
                    <Form.Item label={'Employee Name'}>
                      {getFieldDecorator('employee', {
                        rules: [
                          {
                            required: true,
                            message: 'Input something!',
                          },
                        ],
                      })(<Input  style={{background: '#d6cbd3'}} />)}
                    </Form.Item>
                     <Form.Item label={'Address of Employee'}>
                      {getFieldDecorator('address', {
                        rules: [
                          {
                            required: true,
                            message: 'Input something!',
                          },
                        ],
                      })(<Input  style={{background: '#eca1a6'}} />)}
                    </Form.Item>
                    <Form.Item label={'Company Name'}>
                      {getFieldDecorator('company', {
                        rules: [
                          {
                            required: true,
                            message: 'Input something!',
                          },
                        ],
                      })(<Input  style={{background: '#bdcebe'}}/>)}
                    </Form.Item>
                    <Form.Item label={'Role Ref'}>
                      {getFieldDecorator('role', 
                        {
                          initialValue: "lucy",
                          rules: [
                            {
                              required: true,
                              message: 'Input something!',
                            },
                          ],
                      })(<Select className="role-select">
                          <Option value="jack">Jack</Option>
                          <Option value="lucy">Lucy</Option>
                          <Option value="disabled" disabled>
                            Disabled
                          </Option>
                          <Option value="Yiminghe">yiminghe</Option>
                        </Select>)}
                    </Form.Item>

                        <Form.Item label={'Date of Agreement'}>
                          {getFieldDecorator('agreement', {
                            rules: [
                              {
                                required: true,
                                message: 'Input something!',
                              },
                            ],
                          })(<DatePicker className="agreement-datepicker" format={dateFormat} />)}
                        </Form.Item>

                          <Form.Item label={'Start Date'}>
                            {getFieldDecorator('start', {
                              rules: [
                                {
                                  required: true,
                                  message: 'Input something!',
                                },
                              ],
                            })(<DatePicker className="start-datepicker" format={dateFormat} />)}
                          </Form.Item>

                          <Form.Item label={'End Date'}>
                            {getFieldDecorator('end', {
                              rules: [
                                {
                                  required: true,
                                  message: 'Input something!',
                                },
                              ],
                            })(<DatePicker className="end-datepicker" format={dateFormat} />)}
                          </Form.Item>

                        <Form.Item label={'Base Salary'}>
                          {getFieldDecorator('salary', {
                            rules: [
                              {
                                required: true,
                                message: 'Input something!',
                              },
                            ],
                          })(<Input  style={{background: '#b5e7a0'}}/>)}
                        </Form.Item>

                        <Form.Item label={'Bonus'}>
                          {getFieldDecorator('bonus', {
                            rules: [
                              {
                                required: true,
                                message: 'Input something!',
                              },
                            ],
                          })(<Input style={{background: '#80ced6'}}  />)}
                        </Form.Item>

                        <Form.Item label={'Other Compensation'}>
                          {getFieldDecorator('other', {
                            rules: [
                              {
                                required: true,
                                message: 'Input something!',
                              },
                            ],
                          })(<Input  style={{background: '#c1502e'}}/>)}
                        </Form.Item>

                        <Form.Item label={'Supervisor Information'}>
                          {getFieldDecorator('supervisor', {
                            rules: [
                              {
                                required: true,
                                message: 'Input something!',
                              },
                            ],
                          })(<Input style={{background: '#b1cbbb'}}  />)}
                        </Form.Item>

                        <Form.Item label={'Notice Period'} className="notice-datepicker">
                          {getFieldDecorator('notice', {
                            rules: [
                              {
                                required: true,
                                message: 'Input something!',
                              },
                            ],
                          })(<RangePicker  
                                format={dateFormat}
                              />)}
                        </Form.Item>

                        <Form.Item label={'Non Monetary Benefits'}>
                          {getFieldDecorator('monetary', {
                            rules: [
                              {
                                required: true,
                                message: 'Input something!',
                              },
                            ],
                          })(<Input  style={{background: '#e06377'}} />)}
                        </Form.Item>

                        <Form.Item label={'Health Insuarance'}>
                          {getFieldDecorator('health', {
                            rules: [
                              {
                                required: true,
                                message: 'Input something!',
                              },
                            ],
                          })(<Input  style={{background: '#b34f90'}} />)}
                        </Form.Item>

                        <Form.Item label={'401k'}>
                          {getFieldDecorator('401k', {
                            rules: [
                              {
                                required: true,
                                message: 'Input something!',
                              },
                            ],
                          })(<Input  style={{background: '#ffcc5c'}}/>)}
                        </Form.Item>

                        <Form.Item label={'At will'}>
                          {getFieldDecorator('will', {
                            rules: [
                              {
                                required: true,
                                message: 'Input something!',
                              },
                            ],
                          })(<Input  style={{background: '#588c7e'}}/>)}
                        </Form.Item>
       
                        <Form.Item label={'Stock'}>
                          {getFieldDecorator('stock', {
                            rules: [
                              {
                                required: true,
                                message: 'Input something!',
                              },
                            ],
                          })(<Input  style={{background: '#738ce3'}}/>)}
                        </Form.Item>

                        <Form.Item label={'Vacation'}>
                          {getFieldDecorator('vacation', {
                            rules: [
                              {
                                required: true,
                                message: 'Input something!',
                              },
                            ],
                          })(<Input  style={{background: '#f278b9'}}/>)}
                        </Form.Item>

                    <Row style={{marginTop: 20}}>
                      <Col span={24} style={{ textAlign: 'right' }}>
                        <Button type="primary" htmlType="submit">
                          Submit
                        </Button>
                        <Button style={{ marginLeft: 8 }} onClick={this.handleReset}>
                          Clear
                        </Button>
                      </Col>
                    </Row>
                  </Form>
              </Col>
          }
      </Row>
      
    );
  }
}

const DocEditForm = Form.create({ name: 'advanced_search' })(BasicForm);

export default DocEditForm