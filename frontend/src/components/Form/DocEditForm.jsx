import React from 'react';
import { Form, Row, Col, Input, Button, DatePicker, Select, Affix, message} from 'antd';
import moment from 'moment';

import './DocEditForm.css'

const { Option } = Select;

const dateFormat = 'DD-MM-YYYY';

const formItemLayout = {
  labelCol: {
    xs: { span: 24 },
    sm: { span: 6 },
  },
  wrapperCol: {
    xs: { span: 24 },
    sm: { span: 18 },
  },
};

class BasicForm extends React.Component {
  state = {
    expand: false,
  };

  handleReset = () => {
    let fields = this.props.form.getFieldsValue()
    Object.keys(fields).map(f => fields[f] = undefined)
    this.props.form.setFieldsValue(fields)
  };

  toggle = () => {
    const { expand } = this.state;
    this.setState({ expand: !expand });
  };

  handleSubmit = e => {
    e.preventDefault();
    this.props.form.validateFields((err, values) => {

      if (!err) {
        this.props.updateInfo(values)
      } else {
        message.error('Input error');
      }

    });
  };

  render() {
    let docVisible = this.props.docVisible;
    let formVisible = this.props.formVisible;

    const { getFieldDecorator } = this.props.form;
    let result = this.props.data || {}

    let data = result.data || {}
    let htmlSrc = result.html || ''
    let roles = result.roles || []
    let selectedRole = ''

    const RoleOptions = roles.map((option, index) => {
      if(data.Role_ref === option.id)
        selectedRole = option.Role_Name

      if(option.Role_Name != null)
        return(<Option key={index} value={option.Role_Name}>{option.Role_Name}</Option>)
    })

    return (
      <Row gutter={10} style={{marginTop: 10}}>
          {
            docVisible && formVisible &&
            <Col span={12}>
                <Affix offsetTop={80}>
                  <div className="preview-doc" dangerouslySetInnerHTML={{__html: htmlSrc}}></div>
                </Affix>
            </Col>
          }
          {
            docVisible && !formVisible &&
            <Col span={24}>
                <div className='border-doc' dangerouslySetInnerHTML={{__html: htmlSrc}}></div>
            </Col>
          }
          {
            docVisible && formVisible &&
              <Col span={12}>
                <Form {...formItemLayout} onSubmit={this.handleSubmit} className="doc-edit-form">
                  <Form.Item label={'Document Title'}>
                    {getFieldDecorator('document', {
                      initialValue: data.Document_Name,
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
                      initialValue: data.Employee_Name,
                      rules: [
                        {
                          required: true,
                          message: 'Input something!',
                        },
                      ],
                    })(<Input  style={{background: '#d6cbd3'}} />)}
                  </Form.Item>
                   <Form.Item label={'Address of Employee'}>
                    {getFieldDecorator('emp_address', {
                      initialValue: data.Address_of_Employee,
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
                      initialValue: data.Company_Name,
                      rules: [
                        {
                          required: true,
                          message: 'Input something!',
                        },
                      ],
                    })(<Input  style={{background: '#bdcebe'}}/>)}
                  </Form.Item>
                  <Form.Item label={'Address of Company'}>
                    {getFieldDecorator('com_address', {
                      initialValue: data.Address_of_Company,
                      rules: [
                        {
                          required: true,
                          message: 'Input something!',
                        },
                      ],
                    })(<Input  style={{background: '#eca1a6'}} />)}
                  </Form.Item>
                  <Form.Item label={'Role Ref'}>
                    {getFieldDecorator('role', 
                      {
                        initialValue: data.Roles,
                        rules: [
                          {
                            required: true,
                            message: 'Input something!',
                          },
                        ],
                    })(<Select className="role-select">
                        {RoleOptions}
                      </Select>)}
                  </Form.Item>

                      <Form.Item label={'Date of Agreement'}>
                        {getFieldDecorator('agreement', {
                          initialValue: (data.Date_of_Agreement !== 'None' && data.Date_of_Agreement !== undefined)? moment(new Date(data.Date_of_Agreement), dateFormat): null,
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
                            initialValue: (data.Start_Date !== 'None' && data.Start_Date !== undefined)? moment(new Date(data.Start_Date), dateFormat): null,
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
                            initialValue: (data.End_Date !== 'None' && data.End_Date !== undefined)? moment(new Date(data.End_Date), dateFormat): null,
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
                          initialValue: data.Base_Salary,
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
                          initialValue: data.Bonus,
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
                          initialValue: data.Other_Compensation,
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
                          initialValue: data.Supervisor_Information,
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
                          initialValue: data.Notice_Period,
                          rules: [
                            {
                              required: true,
                              message: 'Input something!',
                            },
                          ],
                        })(<Input style={{background: '#c1cfa5'}}  />)}
                      </Form.Item>

                      <Form.Item label={'Non Monetary Benefits'}>
                        {getFieldDecorator('monetary', {
                          initialValue: data.Non_Monetary_Benefits,
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
                          initialValue: data.Health_Insurance,
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
                          initialValue: data._401k,
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
                          initialValue: data.At_will,
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
                          initialValue: data.Stock,
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
                          initialValue: data.Vacation,
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

          {
            !docVisible && formVisible && 
              <Form {...formItemLayout} onSubmit={this.handleSubmit} className="doc-edit-form">
                <Row gutter={30}>
                  <Col xs={24} sm={12}>
                    <Form.Item label={'Document Title'}>
                      {getFieldDecorator('document', {
                        initialValue: data.Document_Name,
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
                        initialValue: data.Employee_Name,
                        rules: [
                          {
                            required: true,
                            message: 'Input something!',
                          },
                        ],
                      })(<Input  style={{background: '#d6cbd3'}} />)}
                    </Form.Item>
                    <Form.Item label={'Address of Employee'}>
                      {getFieldDecorator('emp_address', {
                        initialValue: data.Address_of_Employee,
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
                        initialValue: data.Company_Name,
                        rules: [
                          {
                            required: true,
                            message: 'Input something!',
                          },
                        ],
                      })(<Input  style={{background: '#bdcebe'}}/>)}
                    </Form.Item>
                    <Form.Item label={'Address of Company'}>
                      {getFieldDecorator('com_address', {
                        initialValue: data.Address_of_Company,
                        rules: [
                          {
                            required: true,
                            message: 'Input something!',
                          },
                        ],
                      })(<Input  style={{background: '#eca1a6'}} />)}
                    </Form.Item>
                    <Form.Item label={'Role Ref'}>
                      {getFieldDecorator('role', 
                        {
                          initialValue: selectedRole,
                          rules: [
                            {
                              required: true,
                              message: 'Input something!',
                            },
                          ],
                      })(<Select className="role-select">
                          {RoleOptions}
                        </Select>)}
                    </Form.Item>

                    <Form.Item label={'Date of Agreement'}>
                      {getFieldDecorator('agreement', {
                        initialValue: (data.Date_of_Agreement !== 'None' && data.Date_of_Agreement !== undefined)? moment(new Date(data.Date_of_Agreement), dateFormat): null,
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
                        initialValue: (data.Start_Date !== 'None' && data.Start_Date !== undefined)? moment(new Date(data.Start_Date), dateFormat): null,
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
                        initialValue: (data.End_Date !== 'None' && data.End_Date !== undefined)? moment(new Date(data.Start_Date), dateFormat): null,
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
                        initialValue: data.Base_Salary,
                        rules: [
                          {
                            required: true,
                            message: 'Input something!',
                          },
                        ],
                      })(<Input  style={{background: '#b5e7a0'}}/>)}
                    </Form.Item>
                    
                  </Col>
                  <Col xs={24} sm={12}>
                    <Form.Item label={'Bonus'}>
                      {getFieldDecorator('bonus', {
                        initialValue: data.Bonus,
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
                        initialValue: data.Other_Compensation,
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
                        initialValue: data.Supervisor_Information,
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
                        initialValue: data.Notice_Period,
                        rules: [
                          {
                            required: true,
                            message: 'Input something!',
                          },
                        ],
                      })(<Input style={{background: '#c1cfa5'}}  />)}
                    </Form.Item>
                    <Form.Item label={'Non Monetary Benefits'}>
                      {getFieldDecorator('monetary', {
                        initialValue: data.Non_Monetary_Benefits,
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
                        initialValue: data.Health_Insurance,
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
                        initialValue: data._401k,
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
                        initialValue: data.At_will,
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
                        initialValue: data.Stock,
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
                        initialValue: data.Vacation,
                        rules: [
                          {
                            required: true,
                            message: 'Input something!',
                          },
                        ],
                      })(<Input  style={{background: '#f278b9'}}/>)}
                    </Form.Item>
                  </Col>
                </Row>
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
          }
      </Row>
      
    );
  }
}

const DocEditForm = Form.create({ name: 'advanced_search' })(BasicForm);

export default DocEditForm