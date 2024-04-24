import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Ice.BO.BAQDesignerSvc
// Description: BAQ designer service
// Version: v1



//////////////////////////////////////////////////////////////////////////
// OData methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => application/json
   */  
export function getServiceDocument(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<JSON>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as JSON)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: Returns metadata document => content
   */  
export function get_metadata(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get BAQDesigners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BAQDesigners
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.DynamicQueryDesignerRow
   */  
export function get_BAQDesigners(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_DynamicQueryDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/BAQDesigners", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_DynamicQueryDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BAQDesigners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.DynamicQueryDesignerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.DynamicQueryDesignerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BAQDesigners(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/BAQDesigners", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the BAQDesigner item
   Description: Calls GetByID to retrieve the BAQDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BAQDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.DynamicQueryDesignerRow
   */  
export function get_BAQDesigners_Company_QueryID(Company:string, QueryID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_DynamicQueryDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/BAQDesigners(" + Company + "," + QueryID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_DynamicQueryDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update BAQDesigner for the service
   Description: Calls UpdateExt to update BAQDesigner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BAQDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.DynamicQueryDesignerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_BAQDesigners_Company_QueryID(Company:string, QueryID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/BAQDesigners(" + Company + "," + QueryID + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete BAQDesigner item
   Description: Call UpdateExt to delete BAQDesigner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BAQDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_BAQDesigners_Company_QueryID(Company:string, QueryID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/BAQDesigners(" + Company + "," + QueryID + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QueryCtrlDesigners items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryCtrlDesigners1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryCtrlDesignerRow
   */  
export function get_BAQDesigners_Company_QueryID_QueryCtrlDesigners(Company:string, QueryID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryCtrlDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/BAQDesigners(" + Company + "," + QueryID + ")/QueryCtrlDesigners", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryCtrlDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryCtrlDesigner item
   Description: Calls GetByID to retrieve the QueryCtrlDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryCtrlDesigner1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param ControlID Desc: ControlID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryCtrlDesignerRow
   */  
export function get_BAQDesigners_Company_QueryID_QueryCtrlDesigners_Company_QueryID_ControlID(Company:string, QueryID:string, ControlID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryCtrlDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/BAQDesigners(" + Company + "," + QueryID + ")/QueryCtrlDesigners(" + Company + "," + QueryID + "," + ControlID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryCtrlDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QueryCustomActionDesigners items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryCustomActionDesigners1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryCustomActionDesignerRow
   */  
export function get_BAQDesigners_Company_QueryID_QueryCustomActionDesigners(Company:string, QueryID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryCustomActionDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/BAQDesigners(" + Company + "," + QueryID + ")/QueryCustomActionDesigners", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryCustomActionDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryCustomActionDesigner item
   Description: Calls GetByID to retrieve the QueryCustomActionDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryCustomActionDesigner1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param ActionID Desc: ActionID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryCustomActionDesignerRow
   */  
export function get_BAQDesigners_Company_QueryID_QueryCustomActionDesigners_Company_QueryID_ActionID(Company:string, QueryID:string, ActionID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryCustomActionDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/BAQDesigners(" + Company + "," + QueryID + ")/QueryCustomActionDesigners(" + Company + "," + QueryID + "," + ActionID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryCustomActionDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QueryExecuteSettingDesigners items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryExecuteSettingDesigners1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryExecuteSettingDesignerRow
   */  
export function get_BAQDesigners_Company_QueryID_QueryExecuteSettingDesigners(Company:string, QueryID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryExecuteSettingDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/BAQDesigners(" + Company + "," + QueryID + ")/QueryExecuteSettingDesigners", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryExecuteSettingDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryExecuteSettingDesigner item
   Description: Calls GetByID to retrieve the QueryExecuteSettingDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryExecuteSettingDesigner1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SettingID Desc: SettingID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryExecuteSettingDesignerRow
   */  
export function get_BAQDesigners_Company_QueryID_QueryExecuteSettingDesigners_Company_QueryID_SettingID(Company:string, QueryID:string, SettingID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryExecuteSettingDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/BAQDesigners(" + Company + "," + QueryID + ")/QueryExecuteSettingDesigners(" + Company + "," + QueryID + "," + SettingID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryExecuteSettingDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QueryParameterDesigners items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryParameterDesigners1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryParameterDesignerRow
   */  
export function get_BAQDesigners_Company_QueryID_QueryParameterDesigners(Company:string, QueryID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryParameterDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/BAQDesigners(" + Company + "," + QueryID + ")/QueryParameterDesigners", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryParameterDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryParameterDesigner item
   Description: Calls GetByID to retrieve the QueryParameterDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryParameterDesigner1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param ParameterID Desc: ParameterID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryParameterDesignerRow
   */  
export function get_BAQDesigners_Company_QueryID_QueryParameterDesigners_Company_QueryID_ParameterID(Company:string, QueryID:string, ParameterID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryParameterDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/BAQDesigners(" + Company + "," + QueryID + ")/QueryParameterDesigners(" + Company + "," + QueryID + "," + ParameterID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryParameterDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QueryReferenceDesigners items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryReferenceDesigners1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryReferenceDesignerRow
   */  
export function get_BAQDesigners_Company_QueryID_QueryReferenceDesigners(Company:string, QueryID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryReferenceDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/BAQDesigners(" + Company + "," + QueryID + ")/QueryReferenceDesigners", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryReferenceDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryReferenceDesigner item
   Description: Calls GetByID to retrieve the QueryReferenceDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryReferenceDesigner1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param ReferenceID Desc: ReferenceID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryReferenceDesignerRow
   */  
export function get_BAQDesigners_Company_QueryID_QueryReferenceDesigners_Company_QueryID_ReferenceID(Company:string, QueryID:string, ReferenceID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryReferenceDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/BAQDesigners(" + Company + "," + QueryID + ")/QueryReferenceDesigners(" + Company + "," + QueryID + "," + ReferenceID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryReferenceDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QuerySubQueryDesigners items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuerySubQueryDesigners1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QuerySubQueryDesignerRow
   */  
export function get_BAQDesigners_Company_QueryID_QuerySubQueryDesigners(Company:string, QueryID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QuerySubQueryDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/BAQDesigners(" + Company + "," + QueryID + ")/QuerySubQueryDesigners", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QuerySubQueryDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuerySubQueryDesigner item
   Description: Calls GetByID to retrieve the QuerySubQueryDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuerySubQueryDesigner1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QuerySubQueryDesignerRow
   */  
export function get_BAQDesigners_Company_QueryID_QuerySubQueryDesigners_Company_QueryID_SubQueryID(Company:string, QueryID:string, SubQueryID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QuerySubQueryDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/BAQDesigners(" + Company + "," + QueryID + ")/QuerySubQueryDesigners(" + Company + "," + QueryID + "," + SubQueryID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_QuerySubQueryDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QueryUpdateFieldDesigners items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryUpdateFieldDesigners1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryUpdateFieldDesignerRow
   */  
export function get_BAQDesigners_Company_QueryID_QueryUpdateFieldDesigners(Company:string, QueryID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryUpdateFieldDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/BAQDesigners(" + Company + "," + QueryID + ")/QueryUpdateFieldDesigners", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryUpdateFieldDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryUpdateFieldDesigner item
   Description: Calls GetByID to retrieve the QueryUpdateFieldDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryUpdateFieldDesigner1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param MapTableName Desc: MapTableName   Required: True   Allow empty value : True
      @param MapFieldName Desc: MapFieldName   Required: True   Allow empty value : True
      @param Direction Desc: Direction   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryUpdateFieldDesignerRow
   */  
export function get_BAQDesigners_Company_QueryID_QueryUpdateFieldDesigners_Company_QueryID_MapTableName_MapFieldName_Direction(Company:string, QueryID:string, MapTableName:string, MapFieldName:string, Direction:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryUpdateFieldDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/BAQDesigners(" + Company + "," + QueryID + ")/QueryUpdateFieldDesigners(" + Company + "," + QueryID + "," + MapTableName + "," + MapFieldName + "," + Direction + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryUpdateFieldDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QueryUpdateSettingsDesigners items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryUpdateSettingsDesigners1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryUpdateSettingsDesignerRow
   */  
export function get_BAQDesigners_Company_QueryID_QueryUpdateSettingsDesigners(Company:string, QueryID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryUpdateSettingsDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/BAQDesigners(" + Company + "," + QueryID + ")/QueryUpdateSettingsDesigners", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryUpdateSettingsDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryUpdateSettingsDesigner item
   Description: Calls GetByID to retrieve the QueryUpdateSettingsDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryUpdateSettingsDesigner1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryUpdateSettingsDesignerRow
   */  
export function get_BAQDesigners_Company_QueryID_QueryUpdateSettingsDesigners_Company_QueryID(Company:string, QueryID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryUpdateSettingsDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/BAQDesigners(" + Company + "," + QueryID + ")/QueryUpdateSettingsDesigners(" + Company + "," + QueryID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryUpdateSettingsDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QueryValueSetItemsDesigners items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryValueSetItemsDesigners1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryValueSetItemsDesignerRow
   */  
export function get_BAQDesigners_Company_QueryID_QueryValueSetItemsDesigners(Company:string, QueryID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryValueSetItemsDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/BAQDesigners(" + Company + "," + QueryID + ")/QueryValueSetItemsDesigners", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryValueSetItemsDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryValueSetItemsDesigner item
   Description: Calls GetByID to retrieve the QueryValueSetItemsDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryValueSetItemsDesigner1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param ValueSetID Desc: ValueSetID   Required: True   Allow empty value : True
      @param ItemValue Desc: ItemValue   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryValueSetItemsDesignerRow
   */  
export function get_BAQDesigners_Company_QueryID_QueryValueSetItemsDesigners_Company_QueryID_ValueSetID_ItemValue(Company:string, QueryID:string, ValueSetID:string, ItemValue:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryValueSetItemsDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/BAQDesigners(" + Company + "," + QueryID + ")/QueryValueSetItemsDesigners(" + Company + "," + QueryID + "," + ValueSetID + "," + ItemValue + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryValueSetItemsDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QueryCtrlDesigners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryCtrlDesigners
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryCtrlDesignerRow
   */  
export function get_QueryCtrlDesigners(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryCtrlDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryCtrlDesigners", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryCtrlDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QueryCtrlDesigners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.QueryCtrlDesignerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.QueryCtrlDesignerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QueryCtrlDesigners(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryCtrlDesigners", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryCtrlDesigner item
   Description: Calls GetByID to retrieve the QueryCtrlDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryCtrlDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param ControlID Desc: ControlID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryCtrlDesignerRow
   */  
export function get_QueryCtrlDesigners_Company_QueryID_ControlID(Company:string, QueryID:string, ControlID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryCtrlDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryCtrlDesigners(" + Company + "," + QueryID + "," + ControlID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryCtrlDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QueryCtrlDesigner for the service
   Description: Calls UpdateExt to update QueryCtrlDesigner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QueryCtrlDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param ControlID Desc: ControlID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.QueryCtrlDesignerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QueryCtrlDesigners_Company_QueryID_ControlID(Company:string, QueryID:string, ControlID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryCtrlDesigners(" + Company + "," + QueryID + "," + ControlID + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QueryCtrlDesigner item
   Description: Call UpdateExt to delete QueryCtrlDesigner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QueryCtrlDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param ControlID Desc: ControlID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QueryCtrlDesigners_Company_QueryID_ControlID(Company:string, QueryID:string, ControlID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryCtrlDesigners(" + Company + "," + QueryID + "," + ControlID + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QueryCtrlValuesDesigners items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryCtrlValuesDesigners1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param ControlID Desc: ControlID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryCtrlValuesDesignerRow
   */  
export function get_QueryCtrlDesigners_Company_QueryID_ControlID_QueryCtrlValuesDesigners(Company:string, QueryID:string, ControlID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryCtrlValuesDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryCtrlDesigners(" + Company + "," + QueryID + "," + ControlID + ")/QueryCtrlValuesDesigners", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryCtrlValuesDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryCtrlValuesDesigner item
   Description: Calls GetByID to retrieve the QueryCtrlValuesDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryCtrlValuesDesigner1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param ControlID Desc: ControlID   Required: True   Allow empty value : True
      @param ID Desc: ID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryCtrlValuesDesignerRow
   */  
export function get_QueryCtrlDesigners_Company_QueryID_ControlID_QueryCtrlValuesDesigners_Company_QueryID_ControlID_ID(Company:string, QueryID:string, ControlID:string, ID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryCtrlValuesDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryCtrlDesigners(" + Company + "," + QueryID + "," + ControlID + ")/QueryCtrlValuesDesigners(" + Company + "," + QueryID + "," + ControlID + "," + ID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryCtrlValuesDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QueryCtrlValuesDesigners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryCtrlValuesDesigners
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryCtrlValuesDesignerRow
   */  
export function get_QueryCtrlValuesDesigners(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryCtrlValuesDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryCtrlValuesDesigners", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryCtrlValuesDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QueryCtrlValuesDesigners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.QueryCtrlValuesDesignerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.QueryCtrlValuesDesignerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QueryCtrlValuesDesigners(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryCtrlValuesDesigners", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryCtrlValuesDesigner item
   Description: Calls GetByID to retrieve the QueryCtrlValuesDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryCtrlValuesDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param ControlID Desc: ControlID   Required: True   Allow empty value : True
      @param ID Desc: ID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryCtrlValuesDesignerRow
   */  
export function get_QueryCtrlValuesDesigners_Company_QueryID_ControlID_ID(Company:string, QueryID:string, ControlID:string, ID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryCtrlValuesDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryCtrlValuesDesigners(" + Company + "," + QueryID + "," + ControlID + "," + ID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryCtrlValuesDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QueryCtrlValuesDesigner for the service
   Description: Calls UpdateExt to update QueryCtrlValuesDesigner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QueryCtrlValuesDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param ControlID Desc: ControlID   Required: True   Allow empty value : True
      @param ID Desc: ID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.QueryCtrlValuesDesignerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QueryCtrlValuesDesigners_Company_QueryID_ControlID_ID(Company:string, QueryID:string, ControlID:string, ID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryCtrlValuesDesigners(" + Company + "," + QueryID + "," + ControlID + "," + ID + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QueryCtrlValuesDesigner item
   Description: Call UpdateExt to delete QueryCtrlValuesDesigner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QueryCtrlValuesDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param ControlID Desc: ControlID   Required: True   Allow empty value : True
      @param ID Desc: ID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QueryCtrlValuesDesigners_Company_QueryID_ControlID_ID(Company:string, QueryID:string, ControlID:string, ID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryCtrlValuesDesigners(" + Company + "," + QueryID + "," + ControlID + "," + ID + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QueryCustomActionDesigners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryCustomActionDesigners
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryCustomActionDesignerRow
   */  
export function get_QueryCustomActionDesigners(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryCustomActionDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryCustomActionDesigners", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryCustomActionDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QueryCustomActionDesigners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.QueryCustomActionDesignerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.QueryCustomActionDesignerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QueryCustomActionDesigners(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryCustomActionDesigners", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryCustomActionDesigner item
   Description: Calls GetByID to retrieve the QueryCustomActionDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryCustomActionDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param ActionID Desc: ActionID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryCustomActionDesignerRow
   */  
export function get_QueryCustomActionDesigners_Company_QueryID_ActionID(Company:string, QueryID:string, ActionID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryCustomActionDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryCustomActionDesigners(" + Company + "," + QueryID + "," + ActionID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryCustomActionDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QueryCustomActionDesigner for the service
   Description: Calls UpdateExt to update QueryCustomActionDesigner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QueryCustomActionDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param ActionID Desc: ActionID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.QueryCustomActionDesignerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QueryCustomActionDesigners_Company_QueryID_ActionID(Company:string, QueryID:string, ActionID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryCustomActionDesigners(" + Company + "," + QueryID + "," + ActionID + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QueryCustomActionDesigner item
   Description: Call UpdateExt to delete QueryCustomActionDesigner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QueryCustomActionDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param ActionID Desc: ActionID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QueryCustomActionDesigners_Company_QueryID_ActionID(Company:string, QueryID:string, ActionID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryCustomActionDesigners(" + Company + "," + QueryID + "," + ActionID + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QueryExecuteSettingDesigners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryExecuteSettingDesigners
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryExecuteSettingDesignerRow
   */  
export function get_QueryExecuteSettingDesigners(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryExecuteSettingDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryExecuteSettingDesigners", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryExecuteSettingDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QueryExecuteSettingDesigners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.QueryExecuteSettingDesignerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.QueryExecuteSettingDesignerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QueryExecuteSettingDesigners(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryExecuteSettingDesigners", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryExecuteSettingDesigner item
   Description: Calls GetByID to retrieve the QueryExecuteSettingDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryExecuteSettingDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SettingID Desc: SettingID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryExecuteSettingDesignerRow
   */  
export function get_QueryExecuteSettingDesigners_Company_QueryID_SettingID(Company:string, QueryID:string, SettingID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryExecuteSettingDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryExecuteSettingDesigners(" + Company + "," + QueryID + "," + SettingID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryExecuteSettingDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QueryExecuteSettingDesigner for the service
   Description: Calls UpdateExt to update QueryExecuteSettingDesigner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QueryExecuteSettingDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SettingID Desc: SettingID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.QueryExecuteSettingDesignerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QueryExecuteSettingDesigners_Company_QueryID_SettingID(Company:string, QueryID:string, SettingID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryExecuteSettingDesigners(" + Company + "," + QueryID + "," + SettingID + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QueryExecuteSettingDesigner item
   Description: Call UpdateExt to delete QueryExecuteSettingDesigner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QueryExecuteSettingDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SettingID Desc: SettingID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QueryExecuteSettingDesigners_Company_QueryID_SettingID(Company:string, QueryID:string, SettingID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryExecuteSettingDesigners(" + Company + "," + QueryID + "," + SettingID + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QueryParameterDesigners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryParameterDesigners
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryParameterDesignerRow
   */  
export function get_QueryParameterDesigners(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryParameterDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryParameterDesigners", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryParameterDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QueryParameterDesigners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.QueryParameterDesignerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.QueryParameterDesignerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QueryParameterDesigners(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryParameterDesigners", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryParameterDesigner item
   Description: Calls GetByID to retrieve the QueryParameterDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryParameterDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param ParameterID Desc: ParameterID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryParameterDesignerRow
   */  
export function get_QueryParameterDesigners_Company_QueryID_ParameterID(Company:string, QueryID:string, ParameterID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryParameterDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryParameterDesigners(" + Company + "," + QueryID + "," + ParameterID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryParameterDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QueryParameterDesigner for the service
   Description: Calls UpdateExt to update QueryParameterDesigner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QueryParameterDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param ParameterID Desc: ParameterID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.QueryParameterDesignerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QueryParameterDesigners_Company_QueryID_ParameterID(Company:string, QueryID:string, ParameterID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryParameterDesigners(" + Company + "," + QueryID + "," + ParameterID + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QueryParameterDesigner item
   Description: Call UpdateExt to delete QueryParameterDesigner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QueryParameterDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param ParameterID Desc: ParameterID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QueryParameterDesigners_Company_QueryID_ParameterID(Company:string, QueryID:string, ParameterID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryParameterDesigners(" + Company + "," + QueryID + "," + ParameterID + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QueryReferenceDesigners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryReferenceDesigners
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryReferenceDesignerRow
   */  
export function get_QueryReferenceDesigners(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryReferenceDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryReferenceDesigners", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryReferenceDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QueryReferenceDesigners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.QueryReferenceDesignerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.QueryReferenceDesignerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QueryReferenceDesigners(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryReferenceDesigners", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryReferenceDesigner item
   Description: Calls GetByID to retrieve the QueryReferenceDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryReferenceDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param ReferenceID Desc: ReferenceID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryReferenceDesignerRow
   */  
export function get_QueryReferenceDesigners_Company_QueryID_ReferenceID(Company:string, QueryID:string, ReferenceID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryReferenceDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryReferenceDesigners(" + Company + "," + QueryID + "," + ReferenceID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryReferenceDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QueryReferenceDesigner for the service
   Description: Calls UpdateExt to update QueryReferenceDesigner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QueryReferenceDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param ReferenceID Desc: ReferenceID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.QueryReferenceDesignerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QueryReferenceDesigners_Company_QueryID_ReferenceID(Company:string, QueryID:string, ReferenceID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryReferenceDesigners(" + Company + "," + QueryID + "," + ReferenceID + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QueryReferenceDesigner item
   Description: Call UpdateExt to delete QueryReferenceDesigner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QueryReferenceDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param ReferenceID Desc: ReferenceID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QueryReferenceDesigners_Company_QueryID_ReferenceID(Company:string, QueryID:string, ReferenceID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryReferenceDesigners(" + Company + "," + QueryID + "," + ReferenceID + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QueryParameterBindingDesigners items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryParameterBindingDesigners1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param ReferenceID Desc: ReferenceID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryParameterBindingDesignerRow
   */  
export function get_QueryReferenceDesigners_Company_QueryID_ReferenceID_QueryParameterBindingDesigners(Company:string, QueryID:string, ReferenceID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryParameterBindingDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryReferenceDesigners(" + Company + "," + QueryID + "," + ReferenceID + ")/QueryParameterBindingDesigners", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryParameterBindingDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryParameterBindingDesigner item
   Description: Calls GetByID to retrieve the QueryParameterBindingDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryParameterBindingDesigner1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param ReferenceID Desc: ReferenceID   Required: True   Allow empty value : True
      @param ParameterID Desc: ParameterID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryParameterBindingDesignerRow
   */  
export function get_QueryReferenceDesigners_Company_QueryID_ReferenceID_QueryParameterBindingDesigners_Company_QueryID_ReferenceID_ParameterID(Company:string, QueryID:string, ReferenceID:string, ParameterID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryParameterBindingDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryReferenceDesigners(" + Company + "," + QueryID + "," + ReferenceID + ")/QueryParameterBindingDesigners(" + Company + "," + QueryID + "," + ReferenceID + "," + ParameterID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryParameterBindingDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QueryParameterBindingDesigners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryParameterBindingDesigners
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryParameterBindingDesignerRow
   */  
export function get_QueryParameterBindingDesigners(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryParameterBindingDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryParameterBindingDesigners", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryParameterBindingDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QueryParameterBindingDesigners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.QueryParameterBindingDesignerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.QueryParameterBindingDesignerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QueryParameterBindingDesigners(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryParameterBindingDesigners", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryParameterBindingDesigner item
   Description: Calls GetByID to retrieve the QueryParameterBindingDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryParameterBindingDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param ReferenceID Desc: ReferenceID   Required: True   Allow empty value : True
      @param ParameterID Desc: ParameterID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryParameterBindingDesignerRow
   */  
export function get_QueryParameterBindingDesigners_Company_QueryID_ReferenceID_ParameterID(Company:string, QueryID:string, ReferenceID:string, ParameterID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryParameterBindingDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryParameterBindingDesigners(" + Company + "," + QueryID + "," + ReferenceID + "," + ParameterID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryParameterBindingDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QueryParameterBindingDesigner for the service
   Description: Calls UpdateExt to update QueryParameterBindingDesigner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QueryParameterBindingDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param ReferenceID Desc: ReferenceID   Required: True   Allow empty value : True
      @param ParameterID Desc: ParameterID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.QueryParameterBindingDesignerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QueryParameterBindingDesigners_Company_QueryID_ReferenceID_ParameterID(Company:string, QueryID:string, ReferenceID:string, ParameterID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryParameterBindingDesigners(" + Company + "," + QueryID + "," + ReferenceID + "," + ParameterID + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QueryParameterBindingDesigner item
   Description: Call UpdateExt to delete QueryParameterBindingDesigner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QueryParameterBindingDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param ReferenceID Desc: ReferenceID   Required: True   Allow empty value : True
      @param ParameterID Desc: ParameterID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QueryParameterBindingDesigners_Company_QueryID_ReferenceID_ParameterID(Company:string, QueryID:string, ReferenceID:string, ParameterID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryParameterBindingDesigners(" + Company + "," + QueryID + "," + ReferenceID + "," + ParameterID + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QuerySubQueryDesigners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuerySubQueryDesigners
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QuerySubQueryDesignerRow
   */  
export function get_QuerySubQueryDesigners(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QuerySubQueryDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QuerySubQueryDesigners", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QuerySubQueryDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuerySubQueryDesigners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.QuerySubQueryDesignerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.QuerySubQueryDesignerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuerySubQueryDesigners(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QuerySubQueryDesigners", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuerySubQueryDesigner item
   Description: Calls GetByID to retrieve the QuerySubQueryDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuerySubQueryDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QuerySubQueryDesignerRow
   */  
export function get_QuerySubQueryDesigners_Company_QueryID_SubQueryID(Company:string, QueryID:string, SubQueryID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QuerySubQueryDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QuerySubQueryDesigners(" + Company + "," + QueryID + "," + SubQueryID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_QuerySubQueryDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QuerySubQueryDesigner for the service
   Description: Calls UpdateExt to update QuerySubQueryDesigner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuerySubQueryDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.QuerySubQueryDesignerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QuerySubQueryDesigners_Company_QueryID_SubQueryID(Company:string, QueryID:string, SubQueryID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QuerySubQueryDesigners(" + Company + "," + QueryID + "," + SubQueryID + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QuerySubQueryDesigner item
   Description: Call UpdateExt to delete QuerySubQueryDesigner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuerySubQueryDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QuerySubQueryDesigners_Company_QueryID_SubQueryID(Company:string, QueryID:string, SubQueryID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QuerySubQueryDesigners(" + Company + "," + QueryID + "," + SubQueryID + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QueryRelationDesigners items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryRelationDesigners1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryRelationDesignerRow
   */  
export function get_QuerySubQueryDesigners_Company_QueryID_SubQueryID_QueryRelationDesigners(Company:string, QueryID:string, SubQueryID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryRelationDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QuerySubQueryDesigners(" + Company + "," + QueryID + "," + SubQueryID + ")/QueryRelationDesigners", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryRelationDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryRelationDesigner item
   Description: Calls GetByID to retrieve the QueryRelationDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryRelationDesigner1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param RelationID Desc: RelationID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryRelationDesignerRow
   */  
export function get_QuerySubQueryDesigners_Company_QueryID_SubQueryID_QueryRelationDesigners_Company_QueryID_SubQueryID_RelationID(Company:string, QueryID:string, SubQueryID:string, RelationID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryRelationDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QuerySubQueryDesigners(" + Company + "," + QueryID + "," + SubQueryID + ")/QueryRelationDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + RelationID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryRelationDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QuerySortByDesigners items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuerySortByDesigners1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QuerySortByDesignerRow
   */  
export function get_QuerySubQueryDesigners_Company_QueryID_SubQueryID_QuerySortByDesigners(Company:string, QueryID:string, SubQueryID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QuerySortByDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QuerySubQueryDesigners(" + Company + "," + QueryID + "," + SubQueryID + ")/QuerySortByDesigners", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QuerySortByDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuerySortByDesigner item
   Description: Calls GetByID to retrieve the QuerySortByDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuerySortByDesigner1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param TableID Desc: TableID   Required: True   Allow empty value : True
      @param FieldName Desc: FieldName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QuerySortByDesignerRow
   */  
export function get_QuerySubQueryDesigners_Company_QueryID_SubQueryID_QuerySortByDesigners_Company_QueryID_SubQueryID_TableID_FieldName(Company:string, QueryID:string, SubQueryID:string, TableID:string, FieldName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QuerySortByDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QuerySubQueryDesigners(" + Company + "," + QueryID + "," + SubQueryID + ")/QuerySortByDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + FieldName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_QuerySortByDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QueryWhereItemDesigners items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryWhereItemDesigners1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryWhereItemDesignerRow
   */  
export function get_QuerySubQueryDesigners_Company_QueryID_SubQueryID_QueryWhereItemDesigners(Company:string, QueryID:string, SubQueryID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryWhereItemDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QuerySubQueryDesigners(" + Company + "," + QueryID + "," + SubQueryID + ")/QueryWhereItemDesigners", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryWhereItemDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryWhereItemDesigner item
   Description: Calls GetByID to retrieve the QueryWhereItemDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryWhereItemDesigner1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param TableID Desc: TableID   Required: True   Allow empty value : True
      @param CriteriaID Desc: CriteriaID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryWhereItemDesignerRow
   */  
export function get_QuerySubQueryDesigners_Company_QueryID_SubQueryID_QueryWhereItemDesigners_Company_QueryID_SubQueryID_TableID_CriteriaID_Seq(Company:string, QueryID:string, SubQueryID:string, TableID:string, CriteriaID:string, Seq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryWhereItemDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QuerySubQueryDesigners(" + Company + "," + QueryID + "," + SubQueryID + ")/QueryWhereItemDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + CriteriaID + "," + Seq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryWhereItemDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QueryGroupByDesigners items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryGroupByDesigners1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryGroupByDesignerRow
   */  
export function get_QuerySubQueryDesigners_Company_QueryID_SubQueryID_QueryGroupByDesigners(Company:string, QueryID:string, SubQueryID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryGroupByDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QuerySubQueryDesigners(" + Company + "," + QueryID + "," + SubQueryID + ")/QueryGroupByDesigners", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryGroupByDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryGroupByDesigner item
   Description: Calls GetByID to retrieve the QueryGroupByDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryGroupByDesigner1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param GroupByID Desc: GroupByID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryGroupByDesignerRow
   */  
export function get_QuerySubQueryDesigners_Company_QueryID_SubQueryID_QueryGroupByDesigners_Company_QueryID_SubQueryID_GroupByID(Company:string, QueryID:string, SubQueryID:string, GroupByID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryGroupByDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QuerySubQueryDesigners(" + Company + "," + QueryID + "," + SubQueryID + ")/QueryGroupByDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + GroupByID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryGroupByDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QueryTableDesigners items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryTableDesigners1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryTableDesignerRow
   */  
export function get_QuerySubQueryDesigners_Company_QueryID_SubQueryID_QueryTableDesigners(Company:string, QueryID:string, SubQueryID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryTableDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QuerySubQueryDesigners(" + Company + "," + QueryID + "," + SubQueryID + ")/QueryTableDesigners", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryTableDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryTableDesigner item
   Description: Calls GetByID to retrieve the QueryTableDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryTableDesigner1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param TableID Desc: TableID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryTableDesignerRow
   */  
export function get_QuerySubQueryDesigners_Company_QueryID_SubQueryID_QueryTableDesigners_Company_QueryID_SubQueryID_TableID(Company:string, QueryID:string, SubQueryID:string, TableID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryTableDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QuerySubQueryDesigners(" + Company + "," + QueryID + "," + SubQueryID + ")/QueryTableDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryTableDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QueryRelationDesigners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryRelationDesigners
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryRelationDesignerRow
   */  
export function get_QueryRelationDesigners(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryRelationDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryRelationDesigners", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryRelationDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QueryRelationDesigners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.QueryRelationDesignerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.QueryRelationDesignerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QueryRelationDesigners(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryRelationDesigners", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryRelationDesigner item
   Description: Calls GetByID to retrieve the QueryRelationDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryRelationDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param RelationID Desc: RelationID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryRelationDesignerRow
   */  
export function get_QueryRelationDesigners_Company_QueryID_SubQueryID_RelationID(Company:string, QueryID:string, SubQueryID:string, RelationID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryRelationDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryRelationDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + RelationID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryRelationDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QueryRelationDesigner for the service
   Description: Calls UpdateExt to update QueryRelationDesigner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QueryRelationDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param RelationID Desc: RelationID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.QueryRelationDesignerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QueryRelationDesigners_Company_QueryID_SubQueryID_RelationID(Company:string, QueryID:string, SubQueryID:string, RelationID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryRelationDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + RelationID + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QueryRelationDesigner item
   Description: Call UpdateExt to delete QueryRelationDesigner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QueryRelationDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param RelationID Desc: RelationID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QueryRelationDesigners_Company_QueryID_SubQueryID_RelationID(Company:string, QueryID:string, SubQueryID:string, RelationID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryRelationDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + RelationID + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QueryRelationFieldDesigners items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryRelationFieldDesigners1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param RelationID Desc: RelationID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryRelationFieldDesignerRow
   */  
export function get_QueryRelationDesigners_Company_QueryID_SubQueryID_RelationID_QueryRelationFieldDesigners(Company:string, QueryID:string, SubQueryID:string, RelationID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryRelationFieldDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryRelationDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + RelationID + ")/QueryRelationFieldDesigners", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryRelationFieldDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryRelationFieldDesigner item
   Description: Calls GetByID to retrieve the QueryRelationFieldDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryRelationFieldDesigner1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param RelationID Desc: RelationID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryRelationFieldDesignerRow
   */  
export function get_QueryRelationDesigners_Company_QueryID_SubQueryID_RelationID_QueryRelationFieldDesigners_Company_QueryID_SubQueryID_RelationID_Seq(Company:string, QueryID:string, SubQueryID:string, RelationID:string, Seq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryRelationFieldDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryRelationDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + RelationID + ")/QueryRelationFieldDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + RelationID + "," + Seq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryRelationFieldDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QueryRelationFieldDesigners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryRelationFieldDesigners
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryRelationFieldDesignerRow
   */  
export function get_QueryRelationFieldDesigners(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryRelationFieldDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryRelationFieldDesigners", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryRelationFieldDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QueryRelationFieldDesigners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.QueryRelationFieldDesignerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.QueryRelationFieldDesignerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QueryRelationFieldDesigners(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryRelationFieldDesigners", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryRelationFieldDesigner item
   Description: Calls GetByID to retrieve the QueryRelationFieldDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryRelationFieldDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param RelationID Desc: RelationID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryRelationFieldDesignerRow
   */  
export function get_QueryRelationFieldDesigners_Company_QueryID_SubQueryID_RelationID_Seq(Company:string, QueryID:string, SubQueryID:string, RelationID:string, Seq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryRelationFieldDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryRelationFieldDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + RelationID + "," + Seq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryRelationFieldDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QueryRelationFieldDesigner for the service
   Description: Calls UpdateExt to update QueryRelationFieldDesigner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QueryRelationFieldDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param RelationID Desc: RelationID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.QueryRelationFieldDesignerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QueryRelationFieldDesigners_Company_QueryID_SubQueryID_RelationID_Seq(Company:string, QueryID:string, SubQueryID:string, RelationID:string, Seq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryRelationFieldDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + RelationID + "," + Seq + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QueryRelationFieldDesigner item
   Description: Call UpdateExt to delete QueryRelationFieldDesigner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QueryRelationFieldDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param RelationID Desc: RelationID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QueryRelationFieldDesigners_Company_QueryID_SubQueryID_RelationID_Seq(Company:string, QueryID:string, SubQueryID:string, RelationID:string, Seq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryRelationFieldDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + RelationID + "," + Seq + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QuerySortByDesigners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuerySortByDesigners
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QuerySortByDesignerRow
   */  
export function get_QuerySortByDesigners(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QuerySortByDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QuerySortByDesigners", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QuerySortByDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuerySortByDesigners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.QuerySortByDesignerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.QuerySortByDesignerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuerySortByDesigners(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QuerySortByDesigners", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuerySortByDesigner item
   Description: Calls GetByID to retrieve the QuerySortByDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuerySortByDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param TableID Desc: TableID   Required: True   Allow empty value : True
      @param FieldName Desc: FieldName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QuerySortByDesignerRow
   */  
export function get_QuerySortByDesigners_Company_QueryID_SubQueryID_TableID_FieldName(Company:string, QueryID:string, SubQueryID:string, TableID:string, FieldName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QuerySortByDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QuerySortByDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + FieldName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_QuerySortByDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QuerySortByDesigner for the service
   Description: Calls UpdateExt to update QuerySortByDesigner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuerySortByDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param TableID Desc: TableID   Required: True   Allow empty value : True
      @param FieldName Desc: FieldName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.QuerySortByDesignerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QuerySortByDesigners_Company_QueryID_SubQueryID_TableID_FieldName(Company:string, QueryID:string, SubQueryID:string, TableID:string, FieldName:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QuerySortByDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + FieldName + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QuerySortByDesigner item
   Description: Call UpdateExt to delete QuerySortByDesigner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuerySortByDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param TableID Desc: TableID   Required: True   Allow empty value : True
      @param FieldName Desc: FieldName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QuerySortByDesigners_Company_QueryID_SubQueryID_TableID_FieldName(Company:string, QueryID:string, SubQueryID:string, TableID:string, FieldName:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QuerySortByDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + FieldName + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QueryWhereItemDesigners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryWhereItemDesigners
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryWhereItemDesignerRow
   */  
export function get_QueryWhereItemDesigners(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryWhereItemDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryWhereItemDesigners", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryWhereItemDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QueryWhereItemDesigners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.QueryWhereItemDesignerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.QueryWhereItemDesignerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QueryWhereItemDesigners(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryWhereItemDesigners", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryWhereItemDesigner item
   Description: Calls GetByID to retrieve the QueryWhereItemDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryWhereItemDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param TableID Desc: TableID   Required: True   Allow empty value : True
      @param CriteriaID Desc: CriteriaID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryWhereItemDesignerRow
   */  
export function get_QueryWhereItemDesigners_Company_QueryID_SubQueryID_TableID_CriteriaID_Seq(Company:string, QueryID:string, SubQueryID:string, TableID:string, CriteriaID:string, Seq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryWhereItemDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryWhereItemDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + CriteriaID + "," + Seq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryWhereItemDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QueryWhereItemDesigner for the service
   Description: Calls UpdateExt to update QueryWhereItemDesigner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QueryWhereItemDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param TableID Desc: TableID   Required: True   Allow empty value : True
      @param CriteriaID Desc: CriteriaID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.QueryWhereItemDesignerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QueryWhereItemDesigners_Company_QueryID_SubQueryID_TableID_CriteriaID_Seq(Company:string, QueryID:string, SubQueryID:string, TableID:string, CriteriaID:string, Seq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryWhereItemDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + CriteriaID + "," + Seq + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QueryWhereItemDesigner item
   Description: Call UpdateExt to delete QueryWhereItemDesigner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QueryWhereItemDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param TableID Desc: TableID   Required: True   Allow empty value : True
      @param CriteriaID Desc: CriteriaID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QueryWhereItemDesigners_Company_QueryID_SubQueryID_TableID_CriteriaID_Seq(Company:string, QueryID:string, SubQueryID:string, TableID:string, CriteriaID:string, Seq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryWhereItemDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + CriteriaID + "," + Seq + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QueryGroupByDesigners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryGroupByDesigners
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryGroupByDesignerRow
   */  
export function get_QueryGroupByDesigners(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryGroupByDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryGroupByDesigners", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryGroupByDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QueryGroupByDesigners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.QueryGroupByDesignerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.QueryGroupByDesignerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QueryGroupByDesigners(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryGroupByDesigners", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryGroupByDesigner item
   Description: Calls GetByID to retrieve the QueryGroupByDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryGroupByDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param GroupByID Desc: GroupByID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryGroupByDesignerRow
   */  
export function get_QueryGroupByDesigners_Company_QueryID_SubQueryID_GroupByID(Company:string, QueryID:string, SubQueryID:string, GroupByID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryGroupByDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryGroupByDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + GroupByID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryGroupByDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QueryGroupByDesigner for the service
   Description: Calls UpdateExt to update QueryGroupByDesigner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QueryGroupByDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param GroupByID Desc: GroupByID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.QueryGroupByDesignerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QueryGroupByDesigners_Company_QueryID_SubQueryID_GroupByID(Company:string, QueryID:string, SubQueryID:string, GroupByID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryGroupByDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + GroupByID + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QueryGroupByDesigner item
   Description: Call UpdateExt to delete QueryGroupByDesigner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QueryGroupByDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param GroupByID Desc: GroupByID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QueryGroupByDesigners_Company_QueryID_SubQueryID_GroupByID(Company:string, QueryID:string, SubQueryID:string, GroupByID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryGroupByDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + GroupByID + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QueryTableDesigners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryTableDesigners
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryTableDesignerRow
   */  
export function get_QueryTableDesigners(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryTableDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryTableDesigners", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryTableDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QueryTableDesigners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.QueryTableDesignerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.QueryTableDesignerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QueryTableDesigners(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryTableDesigners", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryTableDesigner item
   Description: Calls GetByID to retrieve the QueryTableDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryTableDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param TableID Desc: TableID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryTableDesignerRow
   */  
export function get_QueryTableDesigners_Company_QueryID_SubQueryID_TableID(Company:string, QueryID:string, SubQueryID:string, TableID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryTableDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryTableDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryTableDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QueryTableDesigner for the service
   Description: Calls UpdateExt to update QueryTableDesigner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QueryTableDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param TableID Desc: TableID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.QueryTableDesignerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QueryTableDesigners_Company_QueryID_SubQueryID_TableID(Company:string, QueryID:string, SubQueryID:string, TableID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryTableDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QueryTableDesigner item
   Description: Call UpdateExt to delete QueryTableDesigner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QueryTableDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param TableID Desc: TableID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QueryTableDesigners_Company_QueryID_SubQueryID_TableID(Company:string, QueryID:string, SubQueryID:string, TableID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryTableDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QueryFieldDesigners items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryFieldDesigners1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param TableID Desc: TableID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryFieldDesignerRow
   */  
export function get_QueryTableDesigners_Company_QueryID_SubQueryID_TableID_QueryFieldDesigners(Company:string, QueryID:string, SubQueryID:string, TableID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryFieldDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryTableDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + ")/QueryFieldDesigners", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryFieldDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryFieldDesigner item
   Description: Calls GetByID to retrieve the QueryFieldDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryFieldDesigner1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param TableID Desc: TableID   Required: True   Allow empty value : True
      @param FieldName Desc: FieldName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryFieldDesignerRow
   */  
export function get_QueryTableDesigners_Company_QueryID_SubQueryID_TableID_QueryFieldDesigners_Company_QueryID_SubQueryID_TableID_FieldName(Company:string, QueryID:string, SubQueryID:string, TableID:string, FieldName:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryFieldDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryTableDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + ")/QueryFieldDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + FieldName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryFieldDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QueryFunctionCallDesigners items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryFunctionCallDesigners1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param TableID Desc: TableID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryFunctionCallDesignerRow
   */  
export function get_QueryTableDesigners_Company_QueryID_SubQueryID_TableID_QueryFunctionCallDesigners(Company:string, QueryID:string, SubQueryID:string, TableID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryFunctionCallDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryTableDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + ")/QueryFunctionCallDesigners", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryFunctionCallDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryFunctionCallDesigner item
   Description: Calls GetByID to retrieve the QueryFunctionCallDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryFunctionCallDesigner1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param TableID Desc: TableID   Required: True   Allow empty value : True
      @param FunctionID Desc: FunctionID   Required: True   Allow empty value : True
      @param ParameterName Desc: ParameterName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryFunctionCallDesignerRow
   */  
export function get_QueryTableDesigners_Company_QueryID_SubQueryID_TableID_QueryFunctionCallDesigners_Company_QueryID_SubQueryID_FunctionID_ParameterName(Company:string, QueryID:string, SubQueryID:string, TableID:string, FunctionID:string, ParameterName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryFunctionCallDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryTableDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + ")/QueryFunctionCallDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + FunctionID + "," + ParameterName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryFunctionCallDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QueryFieldDesigners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryFieldDesigners
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryFieldDesignerRow
   */  
export function get_QueryFieldDesigners(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryFieldDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryFieldDesigners", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryFieldDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QueryFieldDesigners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.QueryFieldDesignerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.QueryFieldDesignerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QueryFieldDesigners(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryFieldDesigners", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryFieldDesigner item
   Description: Calls GetByID to retrieve the QueryFieldDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryFieldDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param TableID Desc: TableID   Required: True   Allow empty value : True
      @param FieldName Desc: FieldName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryFieldDesignerRow
   */  
export function get_QueryFieldDesigners_Company_QueryID_SubQueryID_TableID_FieldName(Company:string, QueryID:string, SubQueryID:string, TableID:string, FieldName:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryFieldDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryFieldDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + FieldName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryFieldDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QueryFieldDesigner for the service
   Description: Calls UpdateExt to update QueryFieldDesigner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QueryFieldDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param TableID Desc: TableID   Required: True   Allow empty value : True
      @param FieldName Desc: FieldName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.QueryFieldDesignerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QueryFieldDesigners_Company_QueryID_SubQueryID_TableID_FieldName(Company:string, QueryID:string, SubQueryID:string, TableID:string, FieldName:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryFieldDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + FieldName + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QueryFieldDesigner item
   Description: Call UpdateExt to delete QueryFieldDesigner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QueryFieldDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param TableID Desc: TableID   Required: True   Allow empty value : True
      @param FieldName Desc: FieldName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QueryFieldDesigners_Company_QueryID_SubQueryID_TableID_FieldName(Company:string, QueryID:string, SubQueryID:string, TableID:string, FieldName:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryFieldDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + FieldName + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QueryFieldAttributeDesigners items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryFieldAttributeDesigners1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param TableID Desc: TableID   Required: True   Allow empty value : True
      @param FieldName Desc: FieldName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryFieldAttributeDesignerRow
   */  
export function get_QueryFieldDesigners_Company_QueryID_SubQueryID_TableID_FieldName_QueryFieldAttributeDesigners(Company:string, QueryID:string, SubQueryID:string, TableID:string, FieldName:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryFieldAttributeDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryFieldDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + FieldName + ")/QueryFieldAttributeDesigners", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryFieldAttributeDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryFieldAttributeDesigner item
   Description: Calls GetByID to retrieve the QueryFieldAttributeDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryFieldAttributeDesigner1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param TableID Desc: TableID   Required: True   Allow empty value : True
      @param FieldName Desc: FieldName   Required: True   Allow empty value : True
      @param AttributeName Desc: AttributeName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryFieldAttributeDesignerRow
   */  
export function get_QueryFieldDesigners_Company_QueryID_SubQueryID_TableID_FieldName_QueryFieldAttributeDesigners_Company_QueryID_SubQueryID_TableID_FieldName_AttributeName(Company:string, QueryID:string, SubQueryID:string, TableID:string, FieldName:string, AttributeName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryFieldAttributeDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryFieldDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + FieldName + ")/QueryFieldAttributeDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + FieldName + "," + AttributeName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryFieldAttributeDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QueryFieldAttributeDesigners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryFieldAttributeDesigners
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryFieldAttributeDesignerRow
   */  
export function get_QueryFieldAttributeDesigners(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryFieldAttributeDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryFieldAttributeDesigners", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryFieldAttributeDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QueryFieldAttributeDesigners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.QueryFieldAttributeDesignerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.QueryFieldAttributeDesignerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QueryFieldAttributeDesigners(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryFieldAttributeDesigners", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryFieldAttributeDesigner item
   Description: Calls GetByID to retrieve the QueryFieldAttributeDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryFieldAttributeDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param TableID Desc: TableID   Required: True   Allow empty value : True
      @param FieldName Desc: FieldName   Required: True   Allow empty value : True
      @param AttributeName Desc: AttributeName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryFieldAttributeDesignerRow
   */  
export function get_QueryFieldAttributeDesigners_Company_QueryID_SubQueryID_TableID_FieldName_AttributeName(Company:string, QueryID:string, SubQueryID:string, TableID:string, FieldName:string, AttributeName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryFieldAttributeDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryFieldAttributeDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + FieldName + "," + AttributeName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryFieldAttributeDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QueryFieldAttributeDesigner for the service
   Description: Calls UpdateExt to update QueryFieldAttributeDesigner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QueryFieldAttributeDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param TableID Desc: TableID   Required: True   Allow empty value : True
      @param FieldName Desc: FieldName   Required: True   Allow empty value : True
      @param AttributeName Desc: AttributeName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.QueryFieldAttributeDesignerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QueryFieldAttributeDesigners_Company_QueryID_SubQueryID_TableID_FieldName_AttributeName(Company:string, QueryID:string, SubQueryID:string, TableID:string, FieldName:string, AttributeName:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryFieldAttributeDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + FieldName + "," + AttributeName + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QueryFieldAttributeDesigner item
   Description: Call UpdateExt to delete QueryFieldAttributeDesigner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QueryFieldAttributeDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param TableID Desc: TableID   Required: True   Allow empty value : True
      @param FieldName Desc: FieldName   Required: True   Allow empty value : True
      @param AttributeName Desc: AttributeName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QueryFieldAttributeDesigners_Company_QueryID_SubQueryID_TableID_FieldName_AttributeName(Company:string, QueryID:string, SubQueryID:string, TableID:string, FieldName:string, AttributeName:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryFieldAttributeDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + FieldName + "," + AttributeName + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QueryFunctionCallDesigners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryFunctionCallDesigners
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryFunctionCallDesignerRow
   */  
export function get_QueryFunctionCallDesigners(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryFunctionCallDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryFunctionCallDesigners", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryFunctionCallDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QueryFunctionCallDesigners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.QueryFunctionCallDesignerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.QueryFunctionCallDesignerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QueryFunctionCallDesigners(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryFunctionCallDesigners", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryFunctionCallDesigner item
   Description: Calls GetByID to retrieve the QueryFunctionCallDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryFunctionCallDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param FunctionID Desc: FunctionID   Required: True   Allow empty value : True
      @param ParameterName Desc: ParameterName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryFunctionCallDesignerRow
   */  
export function get_QueryFunctionCallDesigners_Company_QueryID_SubQueryID_FunctionID_ParameterName(Company:string, QueryID:string, SubQueryID:string, FunctionID:string, ParameterName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryFunctionCallDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryFunctionCallDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + FunctionID + "," + ParameterName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryFunctionCallDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QueryFunctionCallDesigner for the service
   Description: Calls UpdateExt to update QueryFunctionCallDesigner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QueryFunctionCallDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param FunctionID Desc: FunctionID   Required: True   Allow empty value : True
      @param ParameterName Desc: ParameterName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.QueryFunctionCallDesignerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QueryFunctionCallDesigners_Company_QueryID_SubQueryID_FunctionID_ParameterName(Company:string, QueryID:string, SubQueryID:string, FunctionID:string, ParameterName:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryFunctionCallDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + FunctionID + "," + ParameterName + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QueryFunctionCallDesigner item
   Description: Call UpdateExt to delete QueryFunctionCallDesigner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QueryFunctionCallDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param FunctionID Desc: FunctionID   Required: True   Allow empty value : True
      @param ParameterName Desc: ParameterName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QueryFunctionCallDesigners_Company_QueryID_SubQueryID_FunctionID_ParameterName(Company:string, QueryID:string, SubQueryID:string, FunctionID:string, ParameterName:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryFunctionCallDesigners(" + Company + "," + QueryID + "," + SubQueryID + "," + FunctionID + "," + ParameterName + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QueryUpdateFieldDesigners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryUpdateFieldDesigners
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryUpdateFieldDesignerRow
   */  
export function get_QueryUpdateFieldDesigners(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryUpdateFieldDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryUpdateFieldDesigners", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryUpdateFieldDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QueryUpdateFieldDesigners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.QueryUpdateFieldDesignerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.QueryUpdateFieldDesignerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QueryUpdateFieldDesigners(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryUpdateFieldDesigners", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryUpdateFieldDesigner item
   Description: Calls GetByID to retrieve the QueryUpdateFieldDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryUpdateFieldDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param MapTableName Desc: MapTableName   Required: True   Allow empty value : True
      @param MapFieldName Desc: MapFieldName   Required: True   Allow empty value : True
      @param Direction Desc: Direction   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryUpdateFieldDesignerRow
   */  
export function get_QueryUpdateFieldDesigners_Company_QueryID_MapTableName_MapFieldName_Direction(Company:string, QueryID:string, MapTableName:string, MapFieldName:string, Direction:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryUpdateFieldDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryUpdateFieldDesigners(" + Company + "," + QueryID + "," + MapTableName + "," + MapFieldName + "," + Direction + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryUpdateFieldDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QueryUpdateFieldDesigner for the service
   Description: Calls UpdateExt to update QueryUpdateFieldDesigner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QueryUpdateFieldDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param MapTableName Desc: MapTableName   Required: True   Allow empty value : True
      @param MapFieldName Desc: MapFieldName   Required: True   Allow empty value : True
      @param Direction Desc: Direction   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.QueryUpdateFieldDesignerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QueryUpdateFieldDesigners_Company_QueryID_MapTableName_MapFieldName_Direction(Company:string, QueryID:string, MapTableName:string, MapFieldName:string, Direction:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryUpdateFieldDesigners(" + Company + "," + QueryID + "," + MapTableName + "," + MapFieldName + "," + Direction + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QueryUpdateFieldDesigner item
   Description: Call UpdateExt to delete QueryUpdateFieldDesigner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QueryUpdateFieldDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param MapTableName Desc: MapTableName   Required: True   Allow empty value : True
      @param MapFieldName Desc: MapFieldName   Required: True   Allow empty value : True
      @param Direction Desc: Direction   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QueryUpdateFieldDesigners_Company_QueryID_MapTableName_MapFieldName_Direction(Company:string, QueryID:string, MapTableName:string, MapFieldName:string, Direction:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryUpdateFieldDesigners(" + Company + "," + QueryID + "," + MapTableName + "," + MapFieldName + "," + Direction + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QueryUpdateSettingsDesigners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryUpdateSettingsDesigners
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryUpdateSettingsDesignerRow
   */  
export function get_QueryUpdateSettingsDesigners(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryUpdateSettingsDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryUpdateSettingsDesigners", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryUpdateSettingsDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QueryUpdateSettingsDesigners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.QueryUpdateSettingsDesignerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.QueryUpdateSettingsDesignerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QueryUpdateSettingsDesigners(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryUpdateSettingsDesigners", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryUpdateSettingsDesigner item
   Description: Calls GetByID to retrieve the QueryUpdateSettingsDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryUpdateSettingsDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryUpdateSettingsDesignerRow
   */  
export function get_QueryUpdateSettingsDesigners_Company_QueryID(Company:string, QueryID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryUpdateSettingsDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryUpdateSettingsDesigners(" + Company + "," + QueryID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryUpdateSettingsDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QueryUpdateSettingsDesigner for the service
   Description: Calls UpdateExt to update QueryUpdateSettingsDesigner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QueryUpdateSettingsDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.QueryUpdateSettingsDesignerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QueryUpdateSettingsDesigners_Company_QueryID(Company:string, QueryID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryUpdateSettingsDesigners(" + Company + "," + QueryID + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QueryUpdateSettingsDesigner item
   Description: Call UpdateExt to delete QueryUpdateSettingsDesigner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QueryUpdateSettingsDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QueryUpdateSettingsDesigners_Company_QueryID(Company:string, QueryID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryUpdateSettingsDesigners(" + Company + "," + QueryID + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QueryValueSetItemsDesigners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryValueSetItemsDesigners
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryValueSetItemsDesignerRow
   */  
export function get_QueryValueSetItemsDesigners(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryValueSetItemsDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryValueSetItemsDesigners", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryValueSetItemsDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QueryValueSetItemsDesigners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.QueryValueSetItemsDesignerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.QueryValueSetItemsDesignerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QueryValueSetItemsDesigners(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryValueSetItemsDesigners", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryValueSetItemsDesigner item
   Description: Calls GetByID to retrieve the QueryValueSetItemsDesigner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryValueSetItemsDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param ValueSetID Desc: ValueSetID   Required: True   Allow empty value : True
      @param ItemValue Desc: ItemValue   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryValueSetItemsDesignerRow
   */  
export function get_QueryValueSetItemsDesigners_Company_QueryID_ValueSetID_ItemValue(Company:string, QueryID:string, ValueSetID:string, ItemValue:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryValueSetItemsDesignerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryValueSetItemsDesigners(" + Company + "," + QueryID + "," + ValueSetID + "," + ItemValue + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryValueSetItemsDesignerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QueryValueSetItemsDesigner for the service
   Description: Calls UpdateExt to update QueryValueSetItemsDesigner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QueryValueSetItemsDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param ValueSetID Desc: ValueSetID   Required: True   Allow empty value : True
      @param ItemValue Desc: ItemValue   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.QueryValueSetItemsDesignerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QueryValueSetItemsDesigners_Company_QueryID_ValueSetID_ItemValue(Company:string, QueryID:string, ValueSetID:string, ItemValue:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryValueSetItemsDesigners(" + Company + "," + QueryID + "," + ValueSetID + "," + ItemValue + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QueryValueSetItemsDesigner item
   Description: Call UpdateExt to delete QueryValueSetItemsDesigner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QueryValueSetItemsDesigner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param ValueSetID Desc: ValueSetID   Required: True   Allow empty value : True
      @param ItemValue Desc: ItemValue   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QueryValueSetItemsDesigners_Company_QueryID_ValueSetID_ItemValue(Company:string, QueryID:string, ValueSetID:string, ItemValue:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/QueryValueSetItemsDesigners(" + Company + "," + QueryID + "," + ValueSetID + "," + ItemValue + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.DynamicQueryDesignerListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_DynamicQueryDesignerListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_DynamicQueryDesignerListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
// Custom methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseDynamicQueryDesigner:string, whereClauseQueryCtrlDesigner:string, whereClauseQueryCtrlValuesDesigner:string, whereClauseQueryCustomActionDesigner:string, whereClauseQueryExecuteSettingDesigner:string, whereClauseQueryParameterDesigner:string, whereClauseQueryReferenceDesigner:string, whereClauseQueryParameterBindingDesigner:string, whereClauseQuerySubQueryDesigner:string, whereClauseQueryRelationDesigner:string, whereClauseQueryRelationFieldDesigner:string, whereClauseQuerySortByDesigner:string, whereClauseQueryWhereItemDesigner:string, whereClauseQueryGroupByDesigner:string, whereClauseQueryTableDesigner:string, whereClauseQueryFieldDesigner:string, whereClauseQueryFieldAttributeDesigner:string, whereClauseQueryFunctionCallDesigner:string, whereClauseQueryUpdateFieldDesigner:string, whereClauseQueryUpdateSettingsDesigner:string, whereClauseQueryValueSetItemsDesigner:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseDynamicQueryDesigner!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDynamicQueryDesigner=" + whereClauseDynamicQueryDesigner
   }
   if(typeof whereClauseQueryCtrlDesigner!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQueryCtrlDesigner=" + whereClauseQueryCtrlDesigner
   }
   if(typeof whereClauseQueryCtrlValuesDesigner!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQueryCtrlValuesDesigner=" + whereClauseQueryCtrlValuesDesigner
   }
   if(typeof whereClauseQueryCustomActionDesigner!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQueryCustomActionDesigner=" + whereClauseQueryCustomActionDesigner
   }
   if(typeof whereClauseQueryExecuteSettingDesigner!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQueryExecuteSettingDesigner=" + whereClauseQueryExecuteSettingDesigner
   }
   if(typeof whereClauseQueryParameterDesigner!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQueryParameterDesigner=" + whereClauseQueryParameterDesigner
   }
   if(typeof whereClauseQueryReferenceDesigner!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQueryReferenceDesigner=" + whereClauseQueryReferenceDesigner
   }
   if(typeof whereClauseQueryParameterBindingDesigner!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQueryParameterBindingDesigner=" + whereClauseQueryParameterBindingDesigner
   }
   if(typeof whereClauseQuerySubQueryDesigner!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQuerySubQueryDesigner=" + whereClauseQuerySubQueryDesigner
   }
   if(typeof whereClauseQueryRelationDesigner!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQueryRelationDesigner=" + whereClauseQueryRelationDesigner
   }
   if(typeof whereClauseQueryRelationFieldDesigner!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQueryRelationFieldDesigner=" + whereClauseQueryRelationFieldDesigner
   }
   if(typeof whereClauseQuerySortByDesigner!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQuerySortByDesigner=" + whereClauseQuerySortByDesigner
   }
   if(typeof whereClauseQueryWhereItemDesigner!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQueryWhereItemDesigner=" + whereClauseQueryWhereItemDesigner
   }
   if(typeof whereClauseQueryGroupByDesigner!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQueryGroupByDesigner=" + whereClauseQueryGroupByDesigner
   }
   if(typeof whereClauseQueryTableDesigner!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQueryTableDesigner=" + whereClauseQueryTableDesigner
   }
   if(typeof whereClauseQueryFieldDesigner!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQueryFieldDesigner=" + whereClauseQueryFieldDesigner
   }
   if(typeof whereClauseQueryFieldAttributeDesigner!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQueryFieldAttributeDesigner=" + whereClauseQueryFieldAttributeDesigner
   }
   if(typeof whereClauseQueryFunctionCallDesigner!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQueryFunctionCallDesigner=" + whereClauseQueryFunctionCallDesigner
   }
   if(typeof whereClauseQueryUpdateFieldDesigner!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQueryUpdateFieldDesigner=" + whereClauseQueryUpdateFieldDesigner
   }
   if(typeof whereClauseQueryUpdateSettingsDesigner!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQueryUpdateSettingsDesigner=" + whereClauseQueryUpdateSettingsDesigner
   }
   if(typeof whereClauseQueryValueSetItemsDesigner!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQueryValueSetItemsDesigner=" + whereClauseQueryValueSetItemsDesigner
   }
   if(typeof pageSize!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pageSize=" + pageSize
   }
   if(typeof absolutePage!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "absolutePage=" + absolutePage
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/GetRows" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(queryID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof queryID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "queryID=" + queryID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/GetByID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      @param whereClause Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      @param pageSize Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      @param absolutePage Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetList(whereClause:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClause!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClause=" + whereClause
   }
   if(typeof pageSize!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pageSize=" + pageSize
   }
   if(typeof absolutePage!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "absolutePage=" + absolutePage
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/GetList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetByIDEx
   Description: GetByID with Mode parameters
   OperationID: GetByIDEx
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByIDEx_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDEx_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByIDEx(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/GetByIDEx", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportQuery
   Description: Commits the DataSet changes to the data store by skipping rules.
   OperationID: ImportQuery
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportQuery_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportQuery_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportQuery(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/ImportQuery", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteByCompanyAndID
   Description: delete specified query from specified company
   OperationID: DeleteByCompanyAndID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByCompanyAndID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByCompanyAndID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteByCompanyAndID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/DeleteByCompanyAndID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetUsedInBAQList
   Description: Get lists  where specified query is used
   OperationID: GetUsedInBAQList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetUsedInBAQList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetUsedInBAQList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetUsedInBAQList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/GetUsedInBAQList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTableList
   Description: Get full list of tables from zDataTable for palette and code editor
   OperationID: GetTableList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTableList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTableList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/GetTableList", {
          method: 'post',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetFieldList
   Description: select physical columns info from db and z-tables
   OperationID: GetFieldList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFieldList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFieldList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFieldList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/GetFieldList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBAQColumnList
   Description: Get BAQ columns list
   OperationID: Get_GetBAQColumnList
      @param queryID Desc: BAQ identifier   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBAQColumnList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetBAQColumnList(queryID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof queryID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "queryID=" + queryID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/GetBAQColumnList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetFirstBAQColumn
   Description: Get first BAQ column
   OperationID: Get_GetFirstBAQColumn
      @param queryID Desc: BAQ identifier   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFirstBAQColumn_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetFirstBAQColumn(queryID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof queryID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "queryID=" + queryID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/GetFirstBAQColumn" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetZTableInfo
   Description: Get table information(description) from z-data
   OperationID: GetZTableInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetZTableInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetZTableInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetZTableInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/GetZTableInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDBTableNameByTableID
   Description: Get table database name from z-data
   OperationID: GetDBTableNameByTableID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDBTableNameByTableID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDBTableNameByTableID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDBTableNameByTableID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/GetDBTableNameByTableID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBOTableFieldList
   Description: Select BO table info from z-tables
   OperationID: GetBOTableFieldList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBOTableFieldList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBOTableFieldList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBOTableFieldList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/GetBOTableFieldList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetExecutionSettings
   Description: Execution settings supported by the dynamic query
   OperationID: GetExecutionSettings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetExecutionSettings_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetExecutionSettings(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/GetExecutionSettings", {
          method: 'post',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSvcList
   OperationID: GetSvcList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSvcList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSvcList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/GetSvcList", {
          method: 'post',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LoadQueryDiagram
   Description: This method returns serialized query diagram for classic BAQ Designer.
   OperationID: LoadQueryDiagram
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LoadQueryDiagram_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadQueryDiagram_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LoadQueryDiagram(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/LoadQueryDiagram", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LoadKineticQueryDiagram
   Description: This method returns serialized query diagram for Kinetic BAQ Designer.
   OperationID: LoadKineticQueryDiagram
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LoadKineticQueryDiagram_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadKineticQueryDiagram_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LoadKineticQueryDiagram(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/LoadKineticQueryDiagram", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteQueryDiagram
   Description: This method deletes query diagram both for classic and kinetic version.
   OperationID: DeleteQueryDiagram
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteQueryDiagram_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteQueryDiagram_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteQueryDiagram(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/DeleteQueryDiagram", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SaveQueryDiagram
   Description: This method saves SOAP-serialized query diagram
   OperationID: SaveQueryDiagram
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SaveQueryDiagram_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SaveQueryDiagram_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SaveQueryDiagram(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/SaveQueryDiagram", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateQueryID
   Description: Check if query name entered is valid
   OperationID: ValidateQueryID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateQueryID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateQueryID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateQueryID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/ValidateQueryID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetQueryCompanyLists
   Description: Check if company can be made global - no such query ids in other companies
   OperationID: GetQueryCompanyLists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetQueryCompanyLists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQueryCompanyLists_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetQueryCompanyLists(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/GetQueryCompanyLists", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AvailableCGCCodes
   Description: Country codes available for company
   OperationID: AvailableCGCCodes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AvailableCGCCodes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AvailableCGCCodes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AvailableCGCCodes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/AvailableCGCCodes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PossibleBONames
   Description: returns list of BOs where query tables are used
   OperationID: PossibleBONames
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PossibleBONames_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PossibleBONames_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PossibleBONames(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/PossibleBONames", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBOTableList
   Description: This method returns the list of tables, belonging to specified business object
   OperationID: GetBOTableList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBOTableList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBOTableList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBOTableList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/GetBOTableList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateQuerySecurityFilters
   Description: Updates security filters for provided query
   OperationID: UpdateQuerySecurityFilters
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateQuerySecurityFilters_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateQuerySecurityFilters_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateQuerySecurityFilters(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/UpdateQuerySecurityFilters", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateQueriesSecurityFiltersByDs
   Description: Iterates through each query refers to specified External Datasource or to any of External Datasources linked to specified External Datasource types
and updates security filters
   OperationID: UpdateQueriesSecurityFiltersByDs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateQueriesSecurityFiltersByDs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateQueriesSecurityFiltersByDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateQueriesSecurityFiltersByDs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/UpdateQueriesSecurityFiltersByDs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RegenUpdatableQueryBpm
   Description: Regenerate Updatable Query Bpm code
   OperationID: RegenUpdatableQueryBpm
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RegenUpdatableQueryBpm_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RegenUpdatableQueryBpm_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RegenUpdatableQueryBpm(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/RegenUpdatableQueryBpm", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method FillDisplayFieldAttributes
   Description: Fills attributes for display fields in query if field properties like FieldLabel differ from system settings.
Method is used by query import and BAQUpgrade routine
   OperationID: FillDisplayFieldAttributes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FillDisplayFieldAttributes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FillDisplayFieldAttributes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FillDisplayFieldAttributes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/FillDisplayFieldAttributes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GenerateASP
   Description: Generate Asp file
   OperationID: GenerateASP
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateASP_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateASP_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateASP(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/GenerateASP", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetASPFields
   Description: Get  Fields list for Asp
   OperationID: GetASPFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetASPFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetASPFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetASPFields(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/GetASPFields", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckSecurityCodeForCurrentCompany
   Description: Check query security code for the current company
   OperationID: CheckSecurityCodeForCurrentCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckSecurityCodeForCurrentCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckSecurityCodeForCurrentCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckSecurityCodeForCurrentCompany(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/CheckSecurityCodeForCurrentCompany", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTableExtensions
   Description: Return extension tables for table schemaName.dbTableName
   OperationID: GetTableExtensions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTableExtensions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTableExtensions_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTableExtensions(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/GetTableExtensions", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetSecurityCodeToSystemQuery
   Description: Overrides security code assigned to system query with passed security code.
System query should exists. If ordinal query found by specified id or nothing found then exception is raised.
Security code should exists. If security code is not found then exception is raised.
   OperationID: SetSecurityCodeToSystemQuery
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetSecurityCodeToSystemQuery_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetSecurityCodeToSystemQuery_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetSecurityCodeToSystemQuery(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/SetSecurityCodeToSystemQuery", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDefaultSecurityCodeOfSystemQuery
   Description: Get default security code assigned to system query with passed security code.
System query should exists. If ordinal query found by specified id or nothing found then exception is raised.
   OperationID: GetDefaultSecurityCodeOfSystemQuery
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDefaultSecurityCodeOfSystemQuery_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultSecurityCodeOfSystemQuery_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDefaultSecurityCodeOfSystemQuery(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/GetDefaultSecurityCodeOfSystemQuery", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ResetCache
   Description: Reset specified server-side caches related to BAQ engine
   OperationID: ResetCache
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ResetCache_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ResetCache_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ResetCache(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/ResetCache", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExportBaq
   OperationID: ExportBaq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportBaq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportBaq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExportBaq(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/ExportBaq", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBAQDataSetByContent
   Description: Get BAQ Designer DataSet by content (array of bytes).
   OperationID: GetBAQDataSetByContent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBAQDataSetByContent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBAQDataSetByContent_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBAQDataSetByContent(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/GetBAQDataSetByContent", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportBaq
   OperationID: ImportBaq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportBaq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportBaq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportBaq(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/ImportBaq", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewDynamicQueryDesigner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDynamicQueryDesigner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDynamicQueryDesigner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDynamicQueryDesigner_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDynamicQueryDesigner(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/GetNewDynamicQueryDesigner", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQueryCtrlDesigner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQueryCtrlDesigner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQueryCtrlDesigner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQueryCtrlDesigner_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQueryCtrlDesigner(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/GetNewQueryCtrlDesigner", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQueryCtrlValuesDesigner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQueryCtrlValuesDesigner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQueryCtrlValuesDesigner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQueryCtrlValuesDesigner_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQueryCtrlValuesDesigner(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/GetNewQueryCtrlValuesDesigner", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQueryCustomActionDesigner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQueryCustomActionDesigner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQueryCustomActionDesigner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQueryCustomActionDesigner_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQueryCustomActionDesigner(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/GetNewQueryCustomActionDesigner", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQueryExecuteSettingDesigner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQueryExecuteSettingDesigner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQueryExecuteSettingDesigner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQueryExecuteSettingDesigner_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQueryExecuteSettingDesigner(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/GetNewQueryExecuteSettingDesigner", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQueryParameterDesigner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQueryParameterDesigner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQueryParameterDesigner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQueryParameterDesigner_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQueryParameterDesigner(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/GetNewQueryParameterDesigner", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQueryReferenceDesigner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQueryReferenceDesigner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQueryReferenceDesigner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQueryReferenceDesigner_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQueryReferenceDesigner(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/GetNewQueryReferenceDesigner", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQueryParameterBindingDesigner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQueryParameterBindingDesigner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQueryParameterBindingDesigner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQueryParameterBindingDesigner_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQueryParameterBindingDesigner(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/GetNewQueryParameterBindingDesigner", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQuerySubQueryDesigner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuerySubQueryDesigner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuerySubQueryDesigner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuerySubQueryDesigner_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQuerySubQueryDesigner(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/GetNewQuerySubQueryDesigner", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQueryRelationDesigner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQueryRelationDesigner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQueryRelationDesigner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQueryRelationDesigner_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQueryRelationDesigner(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/GetNewQueryRelationDesigner", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQueryRelationFieldDesigner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQueryRelationFieldDesigner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQueryRelationFieldDesigner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQueryRelationFieldDesigner_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQueryRelationFieldDesigner(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/GetNewQueryRelationFieldDesigner", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQuerySortByDesigner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuerySortByDesigner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuerySortByDesigner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuerySortByDesigner_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQuerySortByDesigner(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/GetNewQuerySortByDesigner", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQueryWhereItemDesigner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQueryWhereItemDesigner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQueryWhereItemDesigner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQueryWhereItemDesigner_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQueryWhereItemDesigner(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/GetNewQueryWhereItemDesigner", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQueryGroupByDesigner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQueryGroupByDesigner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQueryGroupByDesigner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQueryGroupByDesigner_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQueryGroupByDesigner(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/GetNewQueryGroupByDesigner", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQueryTableDesigner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQueryTableDesigner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQueryTableDesigner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQueryTableDesigner_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQueryTableDesigner(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/GetNewQueryTableDesigner", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQueryFieldDesigner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQueryFieldDesigner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQueryFieldDesigner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQueryFieldDesigner_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQueryFieldDesigner(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/GetNewQueryFieldDesigner", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQueryFieldAttributeDesigner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQueryFieldAttributeDesigner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQueryFieldAttributeDesigner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQueryFieldAttributeDesigner_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQueryFieldAttributeDesigner(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/GetNewQueryFieldAttributeDesigner", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQueryFunctionCallDesigner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQueryFunctionCallDesigner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQueryFunctionCallDesigner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQueryFunctionCallDesigner_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQueryFunctionCallDesigner(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/GetNewQueryFunctionCallDesigner", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQueryUpdateFieldDesigner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQueryUpdateFieldDesigner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQueryUpdateFieldDesigner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQueryUpdateFieldDesigner_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQueryUpdateFieldDesigner(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/GetNewQueryUpdateFieldDesigner", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQueryUpdateSettingsDesigner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQueryUpdateSettingsDesigner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQueryUpdateSettingsDesigner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQueryUpdateSettingsDesigner_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQueryUpdateSettingsDesigner(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/GetNewQueryUpdateSettingsDesigner", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQueryValueSetItemsDesigner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQueryValueSetItemsDesigner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQueryValueSetItemsDesigner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQueryValueSetItemsDesigner_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQueryValueSetItemsDesigner(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/GetNewQueryValueSetItemsDesigner", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteByID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetBySysRowID(id:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof id!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "id=" + id
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/GetBySysRowID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetBySysRowIDs(ids:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof ids!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "ids=" + ids
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/GetBySysRowIDs" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Update(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateExt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetGroupUserList
   Description: This method returns an string with the group access list by user.
   OperationID: GetGroupUserList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGroupUserList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetGroupUserList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQDesignerSvc/GetGroupUserList", {
          method: 'post',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_DynamicQueryDesignerListRow{
   "odatametadata":string,
   "value":Ice_Tablesets_DynamicQueryDesignerListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_DynamicQueryDesignerRow{
   "odatametadata":string,
   "value":Ice_Tablesets_DynamicQueryDesignerRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryCtrlDesignerRow{
   "odatametadata":string,
   "value":Ice_Tablesets_QueryCtrlDesignerRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryCtrlValuesDesignerRow{
   "odatametadata":string,
   "value":Ice_Tablesets_QueryCtrlValuesDesignerRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryCustomActionDesignerRow{
   "odatametadata":string,
   "value":Ice_Tablesets_QueryCustomActionDesignerRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryExecuteSettingDesignerRow{
   "odatametadata":string,
   "value":Ice_Tablesets_QueryExecuteSettingDesignerRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryFieldAttributeDesignerRow{
   "odatametadata":string,
   "value":Ice_Tablesets_QueryFieldAttributeDesignerRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryFieldDesignerRow{
   "odatametadata":string,
   "value":Ice_Tablesets_QueryFieldDesignerRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryFunctionCallDesignerRow{
   "odatametadata":string,
   "value":Ice_Tablesets_QueryFunctionCallDesignerRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryGroupByDesignerRow{
   "odatametadata":string,
   "value":Ice_Tablesets_QueryGroupByDesignerRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryParameterBindingDesignerRow{
   "odatametadata":string,
   "value":Ice_Tablesets_QueryParameterBindingDesignerRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryParameterDesignerRow{
   "odatametadata":string,
   "value":Ice_Tablesets_QueryParameterDesignerRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryReferenceDesignerRow{
   "odatametadata":string,
   "value":Ice_Tablesets_QueryReferenceDesignerRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryRelationDesignerRow{
   "odatametadata":string,
   "value":Ice_Tablesets_QueryRelationDesignerRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryRelationFieldDesignerRow{
   "odatametadata":string,
   "value":Ice_Tablesets_QueryRelationFieldDesignerRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QuerySortByDesignerRow{
   "odatametadata":string,
   "value":Ice_Tablesets_QuerySortByDesignerRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QuerySubQueryDesignerRow{
   "odatametadata":string,
   "value":Ice_Tablesets_QuerySubQueryDesignerRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryTableDesignerRow{
   "odatametadata":string,
   "value":Ice_Tablesets_QueryTableDesignerRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryUpdateFieldDesignerRow{
   "odatametadata":string,
   "value":Ice_Tablesets_QueryUpdateFieldDesignerRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryUpdateSettingsDesignerRow{
   "odatametadata":string,
   "value":Ice_Tablesets_QueryUpdateSettingsDesignerRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryValueSetItemsDesignerRow{
   "odatametadata":string,
   "value":Ice_Tablesets_QueryValueSetItemsDesignerRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryWhereItemDesignerRow{
   "odatametadata":string,
   "value":Ice_Tablesets_QueryWhereItemDesignerRow[],
}

export interface Ice_Tablesets_DynamicQueryDesignerListRow{
      /**  Company  */  
   "Company":string,
      /**  QueryID  */  
   "QueryID":string,
      /**  AuthorID  */  
   "AuthorID":string,
      /**  Description  */  
   "Description":string,
      /**  IsShared  */  
   "IsShared":boolean,
      /**  CGCCode  */  
   "CGCCode":string,
      /**  XCompany  */  
   "XCompany":boolean,
      /**  Updatable  */  
   "Updatable":boolean,
      /**  ExtQuery  */  
   "ExtQuery":boolean,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  SysRowID  */  
   "SysRowID":string,
   "AllCompanies":boolean,
      /**  SecCode  */  
   "SecCode":string,
      /**  UseLiveDB  */  
   "UseLiveDB":boolean,
      /**  LastUpdated  */  
   "LastUpdated":string,
      /**  LastUpdatedBy  */  
   "LastUpdatedBy":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_DynamicQueryDesignerRow{
      /**  Company  */  
   "Company":string,
      /**  QueryID  */  
   "QueryID":string,
      /**  AuthorID  */  
   "AuthorID":string,
      /**  Description  */  
   "Description":string,
      /**  DisplayPhrase  */  
   "DisplayPhrase":string,
      /**  IsShared  */  
   "IsShared":boolean,
      /**  Version  */  
   "Version":string,
      /**  CGCCode  */  
   "CGCCode":string,
      /**  XCompany  */  
   "XCompany":boolean,
      /**  GlbCompany  */  
   "GlbCompany":string,
      /**  Updatable  */  
   "Updatable":boolean,
      /**  ExtQuery  */  
   "ExtQuery":boolean,
      /**  ExtDatasourceName  */  
   "ExtDatasourceName":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  Extension  */  
   "Extension":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  SecCode  */  
   "SecCode":string,
      /**  UseLiveDB  */  
   "UseLiveDB":boolean,
      /**  Comment  */  
   "Comment":string,
      /**  LastUpdated  */  
   "LastUpdated":string,
      /**  LastUpdatedBy  */  
   "LastUpdatedBy":string,
      /**  true if update through BO is not used  */  
   "BPMUpdateOnly":boolean,
   "AllCompanies":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_QueryCtrlDesignerRow{
      /**  Company Code  */  
   "Company":string,
      /**  QueryID  */  
   "QueryID":string,
      /**  GUID for control  */  
   "ControlID":string,
      /**  Data Source  */  
   "DataSource":string,
      /**  Data Type  */  
   "DataType":string,
      /**  Field Format  */  
   "FieldFormat":string,
      /**  Mandatory flag  */  
   "IsMandatory":boolean,
      /**  Default Value  */  
   "DefaultValue":string,
      /**   One of predefined constants:
Standard ? free type editor/date picker, depend on DataType.
RadioSet ? radio button set. Items are specified in QueryCtrlValues table
DropDown ? dropdown list. Items are specified in QueryCtrlValues table
DropDownBAQ ? dropdown list. Information are stored in QueryCtrlValues table with tree rows with Ids:BAQID, BAQDisplayColumn, BAQValueColumn
DropDownUserCodes - dropdown list. Information are stored in QueryCtrlValues table with one row with Id = UserCodeTypeID  */  
   "ControlType":string,
      /**  Type of the datasource 0 - updatable field, 1 - parameter  */  
   "SourceType":number,
      /**  ListSource  */  
   "ListSource":string,
      /**  DisplayColumn  */  
   "DisplayColumn":string,
      /**  ValueColumn  */  
   "ValueColumn":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Seq  */  
   "Seq":number,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_QueryCtrlValuesDesignerRow{
      /**  Company Code  */  
   "Company":string,
      /**  QueryID  */  
   "QueryID":string,
      /**  GUID for control  */  
   "ControlID":string,
      /**  Id pof value record  */  
   "ID":string,
      /**  Value  */  
   "Val":string,
      /**  Sequence number  */  
   "Seq":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_QueryCustomActionDesignerRow{
      /**  Company Code  */  
   "Company":string,
      /**  QueryID  */  
   "QueryID":string,
      /**  Action ID  */  
   "ActionID":string,
      /**  Displayble text for the action  */  
   "ActionLabel":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_QueryExecuteSettingDesignerRow{
      /**  Company  */  
   "Company":string,
      /**  QueryID  */  
   "QueryID":string,
      /**  SettingID  */  
   "SettingID":string,
      /**  SettingValue  */  
   "SettingValue":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_QueryFieldAttributeDesignerRow{
      /**  Company  */  
   "Company":string,
      /**  QueryID  */  
   "QueryID":string,
      /**  SubQueryID  */  
   "SubQueryID":string,
      /**  TableID  */  
   "TableID":string,
      /**  FieldName  */  
   "FieldName":string,
      /**  AttributeName  */  
   "AttributeName":string,
      /**  Value  */  
   "Value":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  Flags whether the attribute was changed by user  */  
   "IsOverriden":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_QueryFieldDesignerRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  QueryID  */  
   "QueryID":string,
      /**  SubQueryID  */  
   "SubQueryID":string,
      /**  TableID  */  
   "TableID":string,
      /**  Field Name  */  
   "FieldName":string,
      /**  Sequence  */  
   "Seq":number,
      /**  DBSchemaName  */  
   "DBSchemaName":string,
      /**  Database Table Name  */  
   "DBTableName":string,
      /**  Database Field Name  */  
   "DBFieldName":string,
      /**  Data Type  */  
   "DataType":string,
      /**  Description  */  
   "Description":string,
      /**  External  */  
   "External":boolean,
      /**  IsCalculated  */  
   "IsCalculated":boolean,
      /**  Formula  */  
   "Formula":string,
      /**  Field Format  */  
   "FieldFormat":string,
      /**  Field Label  */  
   "FieldLabel":string,
      /**  TableID to use with LikeField  */  
   "LikeDataFieldTableID":string,
      /**  Like Data Field Sequence  */  
   "LikeDataFieldSeq":number,
      /**  Aggregation  */  
   "Aggregation":string,
      /**  IsGroupBy  */  
   "IsGroupBy":boolean,
      /**  Use Like  */  
   "UseLike":boolean,
      /**  Like Data Field Name  */  
   "LikeDataFieldName":string,
      /**  Wheither field can be updated  */  
   "Updatable":boolean,
      /**  Raise event on update  */  
   "RaiseEvent":boolean,
      /**  ID of Quick Search assigned to this query field  */  
   "QuickSearchID":string,
      /**  This flag tells whether this display field is used as source of distinct values for drop down list in IW  */  
   "DropDown":boolean,
      /**  Initial expression for updatable field, filled on UBAQ.GetNew  */  
   "UpdInitExpression":string,
      /**  Alias  */  
   "Alias":string,
      /**  IsRequired  */  
   "IsRequired":boolean,
      /**  IsReadOnly  */  
   "IsReadOnly":boolean,
      /**  DefaultValue  */  
   "DefaultValue":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "SubquerySet_Alias":string,
   "SubquerySet_DataType":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_QueryFunctionCallDesignerRow{
      /**  Company  */  
   "Company":string,
      /**  QueryID  */  
   "QueryID":string,
      /**  SubQueryID  */  
   "SubQueryID":string,
      /**  FunctionID  */  
   "FunctionID":string,
      /**  ParameterName  */  
   "ParameterName":string,
      /**  Seq  */  
   "Seq":number,
      /**  Value  */  
   "Value":string,
      /**  DataType  */  
   "DataType":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_QueryGroupByDesignerRow{
      /**  Company  */  
   "Company":string,
      /**  QueryID  */  
   "QueryID":string,
      /**  SubQueryID  */  
   "SubQueryID":string,
      /**  GroupByID  */  
   "GroupByID":string,
      /**  Expression  */  
   "Expression":string,
      /**  Seq  */  
   "Seq":number,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_QueryParameterBindingDesignerRow{
      /**  Company  */  
   "Company":string,
      /**  QueryID  */  
   "QueryID":string,
      /**  ReferenceID  */  
   "ReferenceID":string,
      /**  ParameterID  */  
   "ParameterID":string,
      /**  MappingType  */  
   "MappingType":string,
      /**  MappingValue  */  
   "MappingValue":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_QueryParameterDesignerRow{
      /**  Company Code  */  
   "Company":string,
      /**  QueryID  */  
   "QueryID":string,
      /**  ParameterID  */  
   "ParameterID":string,
      /**  Data type of the parameter  */  
   "ParameterType":string,
      /**  ParameterLabel  */  
   "ParameterLabel":string,
      /**  Skip condition of parameter is not set  */  
   "SkipIfEmpty":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_QueryReferenceDesignerRow{
      /**  Company  */  
   "Company":string,
      /**  QueryID  */  
   "QueryID":string,
      /**  ReferenceID  */  
   "ReferenceID":string,
      /**  ReferenceName  */  
   "ReferenceName":string,
      /**  RefQueryID  */  
   "RefQueryID":string,
      /**  ExecType  */  
   "ExecType":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_QueryRelationDesignerRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  QueryID  */  
   "QueryID":string,
      /**  SubQueryID  */  
   "SubQueryID":string,
      /**  Query Relation ID  */  
   "RelationID":string,
      /**  IsFK  */  
   "IsFK":boolean,
      /**  ParentTableID  */  
   "ParentTableID":string,
      /**  ChildTableID  */  
   "ChildTableID":string,
      /**  "Outer" = outer-join, "" = inner-join  */  
   "JoinType":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "OuterJoin":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_QueryRelationFieldDesignerRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  QueryID  */  
   "QueryID":string,
      /**  SubQueryID  */  
   "SubQueryID":string,
      /**  Query Relation ID  */  
   "RelationID":string,
      /**  Sequence Number  */  
   "Seq":number,
      /**  Parent Field Name  */  
   "ParentFieldName":string,
      /**  ParentFieldDataType  */  
   "ParentFieldDataType":string,
      /**  ParentFieldIsExpr  */  
   "ParentFieldIsExpr":boolean,
      /**  Child Field Name  */  
   "ChildFieldName":string,
      /**  ChildFieldDataType  */  
   "ChildFieldDataType":string,
      /**  ChildFieldIsExpr  */  
   "ChildFieldIsExpr":boolean,
      /**  AndOr  */  
   "AndOr":string,
      /**  Neg  */  
   "Neg":boolean,
      /**  LeftP  */  
   "LeftP":string,
      /**  RightP  */  
   "RightP":string,
      /**  CompOp  */  
   "CompOp":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_QuerySortByDesignerRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  QueryID  */  
   "QueryID":string,
      /**  SubQueryID  */  
   "SubQueryID":string,
      /**  TableID  */  
   "TableID":string,
      /**  Field Name  */  
   "FieldName":string,
      /**  Sequence Number  */  
   "Seq":number,
      /**  IsAsc  */  
   "IsAsc":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "DisplayName":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_QuerySubQueryDesignerRow{
      /**  Company  */  
   "Company":string,
      /**  QueryID  */  
   "QueryID":string,
      /**  SubQueryID  */  
   "SubQueryID":string,
      /**  Name  */  
   "Name":string,
      /**  Type  */  
   "Type":string,
      /**  Seq  */  
   "Seq":number,
      /**  IsUnion  */  
   "IsUnion":boolean,
      /**  LeftP  */  
   "LeftP":string,
      /**  RightP  */  
   "RightP":string,
      /**  SelectListClause  */  
   "SelectListClause":string,
      /**  TopRowExpr  */  
   "TopRowExpr":number,
      /**  TopInPercent  */  
   "TopInPercent":boolean,
      /**  TopWithTies  */  
   "TopWithTies":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  OrderByOffSet  */  
   "OrderByOffSet":string,
      /**  OrderByFetch  */  
   "OrderByFetch":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_QueryTableDesignerRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  QueryID  */  
   "QueryID":string,
      /**  SubQueryID  */  
   "SubQueryID":string,
      /**  TableID  */  
   "TableID":string,
      /**  Sequence Number  */  
   "Seq":number,
      /**  DBSchemaName  */  
   "DBSchemaName":string,
      /**  Database Table Name  */  
   "DBTableName":string,
      /**  TableType  */  
   "TableType":string,
      /**  Summary Table flag  */  
   "IsSummaryTable":boolean,
      /**  IsVisibleInDesigner  */  
   "IsVisibleInDesigner":boolean,
      /**  Modifiers  */  
   "Modifiers":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  PivotFunction  */  
   "PivotFunction":string,
      /**  PivotDataType  */  
   "PivotDataType":string,
      /**  PivotFieldFormat  */  
   "PivotFieldFormat":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_QueryUpdateFieldDesignerRow{
      /**  Company Code  */  
   "Company":string,
      /**  QueryID  */  
   "QueryID":string,
      /**  MapTableName  */  
   "MapTableName":string,
      /**  MapFieldName  */  
   "MapFieldName":string,
      /**  Direction  */  
   "Direction":boolean,
      /**  Expression  */  
   "Expression":string,
      /**  IsKeyField  */  
   "IsKeyField":boolean,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  NetDataType  */  
   "NetDataType":string,
      /**  Shows field description - taken from zDataField  */  
   "Description":string,
      /**  DBTableName + "." + DBFieldName  */  
   "QualifiedName":string,
      /**  Shows if field is required - taken from zDataField  */  
   "Required":boolean,
      /**  Shows field data type - taken from zDataField  */  
   "DataType":string,
   "NullableType":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_QueryUpdateSettingsDesignerRow{
      /**  Company  */  
   "Company":string,
      /**  QueryID  */  
   "QueryID":string,
      /**  AllowAddNew  */  
   "AllowAddNew":boolean,
      /**  AddNewLabel  */  
   "AddNewLabel":string,
      /**  SupportMDR  */  
   "SupportMDR":boolean,
      /**  UpdatableType  */  
   "UpdatableType":string,
      /**  UpdatableBO  */  
   "UpdatableBO":string,
      /**  BOSystemCode  */  
   "BOSystemCode":string,
      /**  UpdateMethod  */  
   "UpdateMethod":string,
      /**  SCUrl  */  
   "SCUrl":string,
      /**  SCWorkflow  */  
   "SCWorkflow":string,
      /**  SCCtxUser  */  
   "SCCtxUser":string,
      /**  SCCtxPwd  */  
   "SCCtxPwd":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  SCUserID  */  
   "SCUserID":string,
      /**  SCPassword  */  
   "SCPassword":string,
      /**  SCCtxUrl  */  
   "SCCtxUrl":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_QueryValueSetItemsDesignerRow{
      /**  Company Code  */  
   "Company":string,
      /**  QueryID  */  
   "QueryID":string,
      /**  ID of set of values. Is referenced by QueryWhereItem record for example.  */  
   "ValueSetID":string,
      /**  Item Value  */  
   "ItemValue":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_QueryWhereItemDesignerRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  QueryID  */  
   "QueryID":string,
      /**  SubQueryID  */  
   "SubQueryID":string,
      /**  TableID  */  
   "TableID":string,
      /**  CriteriaID  */  
   "CriteriaID":string,
      /**  Sequence Number  */  
   "Seq":number,
   "FieldName":string,
      /**  DataType  */  
   "DataType":string,
      /**  Operator to use for relation between left value and right value.  */  
   "CompOp":string,
   "AndOr":string,
   "Neg":boolean,
      /**  LeftP  */  
   "LeftP":string,
      /**  RightP  */  
   "RightP":string,
      /**  Indicates that the ChildField is a contant rather than a database field.  Example: Relationships to Reason requires a reasontype which would be entered as a constant.  */  
   "IsConst":boolean,
      /**  CriteriaType  */  
   "CriteriaType":number,
   "UseHaving":boolean,
      /**  ToTableID  */  
   "ToTableID":string,
   "ToFieldName":string,
      /**  ToDataType  */  
   "ToDataType":string,
   "RValue":string,
      /**  ExtSecurity  */  
   "ExtSecurity":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param crossCompany
   */  
export interface AvailableCGCCodes_input{
   crossCompany:boolean,
}

export interface AvailableCGCCodes_output{
   returnObj:string,
}

   /** Required : 
      @param secCode
   */  
export interface CheckSecurityCodeForCurrentCompany_input{
   secCode:string,
}

export interface CheckSecurityCodeForCurrentCompany_output{
parameters : {
      /**  output parameters  */  
   isSecCodeExists:boolean,
   isSecCodeAvailable:boolean,
}
}

   /** Required : 
      @param company
      @param queryID
   */  
export interface DeleteByCompanyAndID_input{
      /**  Company ID  */  
   company:string,
      /**  Query ID  */  
   queryID:string,
}

export interface DeleteByCompanyAndID_output{
}

   /** Required : 
      @param queryID
   */  
export interface DeleteByID_input{
   queryID:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param queryID
      @param companyID
      @param userID
   */  
export interface DeleteQueryDiagram_input{
      /**  The Query(QueryHdr) ID  */  
   queryID:string,
      /**  The Company) ID  */  
   companyID:string,
      /**  The User ID  */  
   userID:string,
}

export interface DeleteQueryDiagram_output{
}

   /** Required : 
      @param queryId
      @param options
   */  
export interface ExportBaq_input{
   queryId:string,
   options:any,      //schema had no properties on an object.
}

export interface ExportBaq_output{
   returnObj:string,
parameters : {
      /**  output parameters  */  
   options: UNKNOW TYPE(error 2338),
   logResult:any[],
}
}

   /** Required : 
      @param companyID
      @param queryID
   */  
export interface FillDisplayFieldAttributes_input{
   companyID:string,
   queryID:string,
}

export interface FillDisplayFieldAttributes_output{
}

   /** Required : 
      @param pcQueryID
      @param pcFilename
      @param ds
   */  
export interface GenerateASP_input{
   pcQueryID:string,
   pcFilename:string,
   ds:Ice_Tablesets_AspExportFieldTableset[],
}

export interface GenerateASP_output{
}

   /** Required : 
      @param pcQueryID
   */  
export interface GetASPFields_input{
   pcQueryID:string,
}

export interface GetASPFields_output{
   returnObj:Ice_Tablesets_AspExportFieldTableset[],
}

   /** Required : 
      @param queryID
   */  
export interface GetBAQColumnList_input{
      /**  BAQ identifier  */  
   queryID:string,
}

export interface GetBAQColumnList_output{
   returnObj:string,
}

   /** Required : 
      @param contentBytes
   */  
export interface GetBAQDataSetByContent_input{
      /**  Content.  */  
   contentBytes:string,
}

export interface GetBAQDataSetByContent_output{
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param dataTableID
      @param schema
   */  
export interface GetBOTableFieldList_input{
   dataTableID:string,
   schema:string,
}

export interface GetBOTableFieldList_output{
   returnObj:Ice_Tablesets_TableFieldListTableset[],
}

   /** Required : 
      @param boName
   */  
export interface GetBOTableList_input{
      /**  Business Object Name in form SystemCode.BOName  */  
   boName:string,
}

export interface GetBOTableList_output{
   returnObj:Ice_Tablesets_BAQBOTablesTableset[],
parameters : {
      /**  output parameters  */  
   topTableID:string,
}
}

   /** Required : 
      @param queryID
      @param mode
   */  
export interface GetByIDEx_input{
   queryID:string,
   mode:number,
}

export interface GetByIDEx_output{
   returnObj:Ice_Tablesets_BAQDesignerTableset[],
}

   /** Required : 
      @param queryID
   */  
export interface GetByID_input{
   queryID:string,
}

export interface GetByID_output{
   returnObj:Ice_Tablesets_BAQDesignerTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Ice_Tablesets_BAQDesignerTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Ice_Tablesets_BAQDesignerTableset[],
}

   /** Required : 
      @param dataTableID
      @param systemCode
   */  
export interface GetDBTableNameByTableID_input{
      /**  DataTableID  */  
   dataTableID:string,
      /**  DB schema (systemCode)  */  
   systemCode:string,
}

export interface GetDBTableNameByTableID_output{
      /**  true if this information found  */  
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   dbTableName:string,
}
}

   /** Required : 
      @param queryId
   */  
export interface GetDefaultSecurityCodeOfSystemQuery_input{
      /**  Id of system query  */  
   queryId:string,
}

export interface GetDefaultSecurityCodeOfSystemQuery_output{
      /**  Default security code  */  
   returnObj:string,
}

export interface GetExecutionSettings_output{
   returnObj:Ice_Tablesets_ExecSettingListTableset[],
}

   /** Required : 
      @param dataTableID
      @param schema
   */  
export interface GetFieldList_input{
   dataTableID:string,
   schema:string,
}

export interface GetFieldList_output{
   returnObj:Ice_Tablesets_TableFieldListTableset[],
}

   /** Required : 
      @param queryID
   */  
export interface GetFirstBAQColumn_input{
      /**  BAQ identifier  */  
   queryID:string,
}

export interface GetFirstBAQColumn_output{
   returnObj:string,
}

export interface GetGroupUserList_output{
parameters : {
      /**  output parameters  */  
   groupUserList:string,
}
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetList_input{
      /**  An expression used to filter the rows. Can be left blank for all rows.  */  
   whereClause:string,
      /**  The maximum number of rows to return. Leave as zero for no maximum.  */  
   pageSize:number,
      /**  Page of rows to return.  */  
   absolutePage:number,
}

export interface GetList_output{
   returnObj:Ice_Tablesets_BAQDesignerListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewDynamicQueryDesigner_input{
   ds:Ice_Tablesets_BAQDesignerTableset[],
}

export interface GetNewDynamicQueryDesigner_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_BAQDesignerTableset[],
}
}

   /** Required : 
      @param ds
      @param queryID
   */  
export interface GetNewQueryCtrlDesigner_input{
   ds:Ice_Tablesets_BAQDesignerTableset[],
   queryID:string,
}

export interface GetNewQueryCtrlDesigner_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_BAQDesignerTableset[],
}
}

   /** Required : 
      @param ds
      @param queryID
      @param controlID
   */  
export interface GetNewQueryCtrlValuesDesigner_input{
   ds:Ice_Tablesets_BAQDesignerTableset[],
   queryID:string,
   controlID:string,
}

export interface GetNewQueryCtrlValuesDesigner_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_BAQDesignerTableset[],
}
}

   /** Required : 
      @param ds
      @param queryID
   */  
export interface GetNewQueryCustomActionDesigner_input{
   ds:Ice_Tablesets_BAQDesignerTableset[],
   queryID:string,
}

export interface GetNewQueryCustomActionDesigner_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_BAQDesignerTableset[],
}
}

   /** Required : 
      @param ds
      @param queryID
   */  
export interface GetNewQueryExecuteSettingDesigner_input{
   ds:Ice_Tablesets_BAQDesignerTableset[],
   queryID:string,
}

export interface GetNewQueryExecuteSettingDesigner_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_BAQDesignerTableset[],
}
}

   /** Required : 
      @param ds
      @param queryID
      @param subQueryID
      @param tableID
      @param fieldName
   */  
export interface GetNewQueryFieldAttributeDesigner_input{
   ds:Ice_Tablesets_BAQDesignerTableset[],
   queryID:string,
   subQueryID:string,
   tableID:string,
   fieldName:string,
}

export interface GetNewQueryFieldAttributeDesigner_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_BAQDesignerTableset[],
}
}

   /** Required : 
      @param ds
      @param queryID
      @param subQueryID
      @param tableID
   */  
export interface GetNewQueryFieldDesigner_input{
   ds:Ice_Tablesets_BAQDesignerTableset[],
   queryID:string,
   subQueryID:string,
   tableID:string,
}

export interface GetNewQueryFieldDesigner_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_BAQDesignerTableset[],
}
}

   /** Required : 
      @param ds
      @param queryID
      @param subQueryID
      @param functionID
   */  
export interface GetNewQueryFunctionCallDesigner_input{
   ds:Ice_Tablesets_BAQDesignerTableset[],
   queryID:string,
   subQueryID:string,
   functionID:string,
}

export interface GetNewQueryFunctionCallDesigner_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_BAQDesignerTableset[],
}
}

   /** Required : 
      @param ds
      @param queryID
      @param subQueryID
   */  
export interface GetNewQueryGroupByDesigner_input{
   ds:Ice_Tablesets_BAQDesignerTableset[],
   queryID:string,
   subQueryID:string,
}

export interface GetNewQueryGroupByDesigner_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_BAQDesignerTableset[],
}
}

   /** Required : 
      @param ds
      @param queryID
      @param referenceID
   */  
export interface GetNewQueryParameterBindingDesigner_input{
   ds:Ice_Tablesets_BAQDesignerTableset[],
   queryID:string,
   referenceID:string,
}

export interface GetNewQueryParameterBindingDesigner_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_BAQDesignerTableset[],
}
}

   /** Required : 
      @param ds
      @param queryID
   */  
export interface GetNewQueryParameterDesigner_input{
   ds:Ice_Tablesets_BAQDesignerTableset[],
   queryID:string,
}

export interface GetNewQueryParameterDesigner_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_BAQDesignerTableset[],
}
}

   /** Required : 
      @param ds
      @param queryID
   */  
export interface GetNewQueryReferenceDesigner_input{
   ds:Ice_Tablesets_BAQDesignerTableset[],
   queryID:string,
}

export interface GetNewQueryReferenceDesigner_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_BAQDesignerTableset[],
}
}

   /** Required : 
      @param ds
      @param queryID
      @param subQueryID
   */  
export interface GetNewQueryRelationDesigner_input{
   ds:Ice_Tablesets_BAQDesignerTableset[],
   queryID:string,
   subQueryID:string,
}

export interface GetNewQueryRelationDesigner_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_BAQDesignerTableset[],
}
}

   /** Required : 
      @param ds
      @param queryID
      @param subQueryID
      @param relationID
   */  
export interface GetNewQueryRelationFieldDesigner_input{
   ds:Ice_Tablesets_BAQDesignerTableset[],
   queryID:string,
   subQueryID:string,
   relationID:string,
}

export interface GetNewQueryRelationFieldDesigner_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_BAQDesignerTableset[],
}
}

   /** Required : 
      @param ds
      @param queryID
      @param subQueryID
      @param tableID
   */  
export interface GetNewQuerySortByDesigner_input{
   ds:Ice_Tablesets_BAQDesignerTableset[],
   queryID:string,
   subQueryID:string,
   tableID:string,
}

export interface GetNewQuerySortByDesigner_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_BAQDesignerTableset[],
}
}

   /** Required : 
      @param ds
      @param queryID
   */  
export interface GetNewQuerySubQueryDesigner_input{
   ds:Ice_Tablesets_BAQDesignerTableset[],
   queryID:string,
}

export interface GetNewQuerySubQueryDesigner_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_BAQDesignerTableset[],
}
}

   /** Required : 
      @param ds
      @param queryID
      @param subQueryID
   */  
export interface GetNewQueryTableDesigner_input{
   ds:Ice_Tablesets_BAQDesignerTableset[],
   queryID:string,
   subQueryID:string,
}

export interface GetNewQueryTableDesigner_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_BAQDesignerTableset[],
}
}

   /** Required : 
      @param ds
      @param queryID
      @param mapTableName
      @param mapFieldName
   */  
export interface GetNewQueryUpdateFieldDesigner_input{
   ds:Ice_Tablesets_BAQDesignerTableset[],
   queryID:string,
   mapTableName:string,
   mapFieldName:string,
}

export interface GetNewQueryUpdateFieldDesigner_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_BAQDesignerTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewQueryUpdateSettingsDesigner_input{
   ds:Ice_Tablesets_BAQDesignerTableset[],
}

export interface GetNewQueryUpdateSettingsDesigner_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_BAQDesignerTableset[],
}
}

   /** Required : 
      @param ds
      @param queryID
      @param valueSetID
   */  
export interface GetNewQueryValueSetItemsDesigner_input{
   ds:Ice_Tablesets_BAQDesignerTableset[],
   queryID:string,
   valueSetID:string,
}

export interface GetNewQueryValueSetItemsDesigner_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_BAQDesignerTableset[],
}
}

   /** Required : 
      @param ds
      @param queryID
      @param subQueryID
      @param tableID
      @param criteriaID
   */  
export interface GetNewQueryWhereItemDesigner_input{
   ds:Ice_Tablesets_BAQDesignerTableset[],
   queryID:string,
   subQueryID:string,
   tableID:string,
   criteriaID:string,
}

export interface GetNewQueryWhereItemDesigner_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_BAQDesignerTableset[],
}
}

   /** Required : 
      @param queryID
   */  
export interface GetQueryCompanyLists_input{
      /**  query id to check  */  
   queryID:string,
}

export interface GetQueryCompanyLists_output{
parameters : {
      /**  output parameters  */  
   globalInCompany:string,
   localInCompanies:string,
}
}

   /** Required : 
      @param whereClauseDynamicQueryDesigner
      @param whereClauseQueryCtrlDesigner
      @param whereClauseQueryCtrlValuesDesigner
      @param whereClauseQueryCustomActionDesigner
      @param whereClauseQueryExecuteSettingDesigner
      @param whereClauseQueryParameterDesigner
      @param whereClauseQueryReferenceDesigner
      @param whereClauseQueryParameterBindingDesigner
      @param whereClauseQuerySubQueryDesigner
      @param whereClauseQueryRelationDesigner
      @param whereClauseQueryRelationFieldDesigner
      @param whereClauseQuerySortByDesigner
      @param whereClauseQueryWhereItemDesigner
      @param whereClauseQueryGroupByDesigner
      @param whereClauseQueryTableDesigner
      @param whereClauseQueryFieldDesigner
      @param whereClauseQueryFieldAttributeDesigner
      @param whereClauseQueryFunctionCallDesigner
      @param whereClauseQueryUpdateFieldDesigner
      @param whereClauseQueryUpdateSettingsDesigner
      @param whereClauseQueryValueSetItemsDesigner
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseDynamicQueryDesigner:string,
   whereClauseQueryCtrlDesigner:string,
   whereClauseQueryCtrlValuesDesigner:string,
   whereClauseQueryCustomActionDesigner:string,
   whereClauseQueryExecuteSettingDesigner:string,
   whereClauseQueryParameterDesigner:string,
   whereClauseQueryReferenceDesigner:string,
   whereClauseQueryParameterBindingDesigner:string,
   whereClauseQuerySubQueryDesigner:string,
   whereClauseQueryRelationDesigner:string,
   whereClauseQueryRelationFieldDesigner:string,
   whereClauseQuerySortByDesigner:string,
   whereClauseQueryWhereItemDesigner:string,
   whereClauseQueryGroupByDesigner:string,
   whereClauseQueryTableDesigner:string,
   whereClauseQueryFieldDesigner:string,
   whereClauseQueryFieldAttributeDesigner:string,
   whereClauseQueryFunctionCallDesigner:string,
   whereClauseQueryUpdateFieldDesigner:string,
   whereClauseQueryUpdateSettingsDesigner:string,
   whereClauseQueryValueSetItemsDesigner:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Ice_Tablesets_BAQDesignerTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface GetSvcList_output{
   returnObj:Ice_Tablesets_SvcListTableset[],
}

   /** Required : 
      @param schemaName
      @param dbTableName
   */  
export interface GetTableExtensions_input{
      /**  Extended table schema  */  
   schemaName:string,
      /**  Extended table db name  */  
   dbTableName:string,
}

export interface GetTableExtensions_output{
   returnObj:Ice_Contracts_ExtendedTableInfo[],
}

export interface GetTableList_output{
   returnObj:Ice_Tablesets_FullTableListTableset[],
}

   /** Required : 
      @param queryID
      @param isGlobalQuery
   */  
export interface GetUsedInBAQList_input{
      /**  The Query(Exports) ID  */  
   queryID:string,
      /**  isGlobalQuery  */  
   isGlobalQuery:boolean,
}

export interface GetUsedInBAQList_output{
   returnObj:Ice_Tablesets_UsedInBAQListTableset[],
}

   /** Required : 
      @param dbTableName
      @param schema
   */  
export interface GetZTableInfo_input{
      /**  DB Table Name  */  
   dbTableName:string,
      /**  DB schema (systemCode)  */  
   schema:string,
}

export interface GetZTableInfo_output{
      /**  true if this information found  */  
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   description:string,
}
}

export interface Ice_BOUpdErrorRow{
   TableName:string,
   ErrorLevel:string,
   ErrorType:string,
   ErrorText:string,
   ErrorSysRowID:string,
   SysRowID:string,
   RowMod:string,
}

export interface Ice_BOUpdErrorTableset{
   BOUpdError:Ice_BOUpdErrorRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Contracts_ExtendedTableInfo{
   SchemaName:string,
   DBTableName:string,
   ExtensionTables:Ice_Contracts_ExtensionTableInfo[],
}

export interface Ice_Contracts_ExtensionTableInfo{
   SystemCode:string,
   SchemaName:string,
   DBTableName:string,
   TableType:string,
   Relations:Ice_Contracts_ExtensionTableRelationInfo[],
}

export interface Ice_Contracts_ExtensionTableRelationColumnInfo{
   ExtendedTableColumn:string,
   ExtensionTableColumn:string,
   CompOp:string,
}

export interface Ice_Contracts_ExtensionTableRelationInfo{
   RelationID:string,
   ExtensionSchemaName:string,
   ExtensionTableName:string,
   Join:number,
   Columns:Ice_Contracts_ExtensionTableRelationColumnInfo[],
}

export interface Ice_Extensions_ExtensionRow{
   ColumnValues:object
   RowMod:string,
   SysRowID:string,
}

export interface Ice_Extensions_ExtensionTableColumn{
   ColumnName:string,
   ColumnType:string,
}

export interface Ice_Extensions_ExtensionTableData{
   Table:Ice_Extensions_ExtensionRow[],
   SystemCode:string,
   TableName:string,
   Columns:Ice_Extensions_ExtensionTableColumn[],
   PrimaryKeyColumns:string,
   PeerTableSystemCode:string,
   PeerTableName:string,
}

export interface Ice_Tablesets_AspExportFieldRow{
   QueryID:string,
   Seq:number,
   FieldName:string,
   Description:string,
   FieldFormat:string,
   FieldLabel:string,
   FieldOrder:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Company  */  
   Company:string,
   FieldSearch:string,
   SearchOptions:string,
   ShowField:boolean,
   SearchField:boolean,
   IsNumeric:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_AspExportFieldTableset{
   AspExportField:Ice_Tablesets_AspExportFieldRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_BAQBOTablesTableset{
   BAQBOtables:Ice_Tablesets_BAQBOtablesRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_BAQBOtablesRow{
   DataTableID:string,
   ParentTableID:string,
   TableType:string,
   SystemCode:string,
   DBTableName:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_BAQDesignerListTableset{
   DynamicQueryDesignerList:Ice_Tablesets_DynamicQueryDesignerListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_BAQDesignerTableset{
   DynamicQueryDesigner:Ice_Tablesets_DynamicQueryDesignerRow[],
   QueryCtrlDesigner:Ice_Tablesets_QueryCtrlDesignerRow[],
   QueryCtrlValuesDesigner:Ice_Tablesets_QueryCtrlValuesDesignerRow[],
   QueryCustomActionDesigner:Ice_Tablesets_QueryCustomActionDesignerRow[],
   QueryExecuteSettingDesigner:Ice_Tablesets_QueryExecuteSettingDesignerRow[],
   QueryParameterDesigner:Ice_Tablesets_QueryParameterDesignerRow[],
   QueryReferenceDesigner:Ice_Tablesets_QueryReferenceDesignerRow[],
   QueryParameterBindingDesigner:Ice_Tablesets_QueryParameterBindingDesignerRow[],
   QuerySubQueryDesigner:Ice_Tablesets_QuerySubQueryDesignerRow[],
   QueryRelationDesigner:Ice_Tablesets_QueryRelationDesignerRow[],
   QueryRelationFieldDesigner:Ice_Tablesets_QueryRelationFieldDesignerRow[],
   QuerySortByDesigner:Ice_Tablesets_QuerySortByDesignerRow[],
   QueryWhereItemDesigner:Ice_Tablesets_QueryWhereItemDesignerRow[],
   QueryGroupByDesigner:Ice_Tablesets_QueryGroupByDesignerRow[],
   QueryTableDesigner:Ice_Tablesets_QueryTableDesignerRow[],
   QueryFieldDesigner:Ice_Tablesets_QueryFieldDesignerRow[],
   QueryFieldAttributeDesigner:Ice_Tablesets_QueryFieldAttributeDesignerRow[],
   QueryFunctionCallDesigner:Ice_Tablesets_QueryFunctionCallDesignerRow[],
   QueryUpdateFieldDesigner:Ice_Tablesets_QueryUpdateFieldDesignerRow[],
   QueryUpdateSettingsDesigner:Ice_Tablesets_QueryUpdateSettingsDesignerRow[],
   QueryValueSetItemsDesigner:Ice_Tablesets_QueryValueSetItemsDesignerRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_BAQReportListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  BAQ Report ID, the unique identifier for this report within the company  */  
   BAQRptID:string,
      /**  Description  */  
   Description:string,
      /**  Title for this report  */  
   ReportTitle:string,
      /**  The unique export identifier.  */  
   ExportID:string,
      /**  Indicates the report is a system deliver report.  */  
   SystemFlag:boolean,
      /**  true if this report is available to all companies  */  
   GlobalReport:boolean,
      /**  Country Group Code / Country Code for CSF  */  
   CGCCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_DashBdBAQRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  VN - Vantage, VS - Vista  */  
   ProductID:string,
      /**  Global Company identifier.  Used in identify from whch company this BAQ originated.  */  
   GlbCompany:string,
      /**  Dashboard Definition ID  */  
   DefinitionID:string,
      /**  Query ID  */  
   QueryID:string,
      /**  Country Group / Country Code for CSF  */  
   CGCCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_DynamicQueryDesignerListRow{
      /**  Company  */  
   Company:string,
      /**  QueryID  */  
   QueryID:string,
      /**  AuthorID  */  
   AuthorID:string,
      /**  Description  */  
   Description:string,
      /**  IsShared  */  
   IsShared:boolean,
      /**  CGCCode  */  
   CGCCode:string,
      /**  XCompany  */  
   XCompany:boolean,
      /**  Updatable  */  
   Updatable:boolean,
      /**  ExtQuery  */  
   ExtQuery:boolean,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  SysRowID  */  
   SysRowID:string,
   AllCompanies:boolean,
      /**  SecCode  */  
   SecCode:string,
      /**  UseLiveDB  */  
   UseLiveDB:boolean,
      /**  LastUpdated  */  
   LastUpdated:string,
      /**  LastUpdatedBy  */  
   LastUpdatedBy:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_DynamicQueryDesignerRow{
      /**  Company  */  
   Company:string,
      /**  QueryID  */  
   QueryID:string,
      /**  AuthorID  */  
   AuthorID:string,
      /**  Description  */  
   Description:string,
      /**  DisplayPhrase  */  
   DisplayPhrase:string,
      /**  IsShared  */  
   IsShared:boolean,
      /**  Version  */  
   Version:string,
      /**  CGCCode  */  
   CGCCode:string,
      /**  XCompany  */  
   XCompany:boolean,
      /**  GlbCompany  */  
   GlbCompany:string,
      /**  Updatable  */  
   Updatable:boolean,
      /**  ExtQuery  */  
   ExtQuery:boolean,
      /**  ExtDatasourceName  */  
   ExtDatasourceName:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  Extension  */  
   Extension:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  SecCode  */  
   SecCode:string,
      /**  UseLiveDB  */  
   UseLiveDB:boolean,
      /**  Comment  */  
   Comment:string,
      /**  LastUpdated  */  
   LastUpdated:string,
      /**  LastUpdatedBy  */  
   LastUpdatedBy:string,
      /**  true if update through BO is not used  */  
   BPMUpdateOnly:boolean,
   AllCompanies:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ExecSettingListRow{
   SettingID:string,
   SettingType:string,
   DefaultValue:string,
   Required:boolean,
   IsEnum:boolean,
   Description:string,
   Category:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ExecSettingListTableset{
   ExecSettingList:Ice_Tablesets_ExecSettingListRow[],
   ExecSettingValues:Ice_Tablesets_ExecSettingValuesRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_ExecSettingValuesRow{
   SettingID:string,
   SettingEnumValue:string,
   SettingValueOrder:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_FullTableListRow{
      /**  DataTableID from zDataTable  */  
   TableID:string,
      /**  Description from zDataTable  */  
   Description:string,
      /**  DB = Database, TT = Temp Table from ZDataTable  */  
   TableType:string,
      /**  Db Schema of the Database table from Ice.Table view  */  
   DBSchemaName:string,
      /**  Db Schema of the Database table  */  
   FullTableName:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_FullTableListTableset{
   FullTableList:Ice_Tablesets_FullTableListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_QueryCtrlDesignerRow{
      /**  Company Code  */  
   Company:string,
      /**  QueryID  */  
   QueryID:string,
      /**  GUID for control  */  
   ControlID:string,
      /**  Data Source  */  
   DataSource:string,
      /**  Data Type  */  
   DataType:string,
      /**  Field Format  */  
   FieldFormat:string,
      /**  Mandatory flag  */  
   IsMandatory:boolean,
      /**  Default Value  */  
   DefaultValue:string,
      /**   One of predefined constants:
Standard ? free type editor/date picker, depend on DataType.
RadioSet ? radio button set. Items are specified in QueryCtrlValues table
DropDown ? dropdown list. Items are specified in QueryCtrlValues table
DropDownBAQ ? dropdown list. Information are stored in QueryCtrlValues table with tree rows with Ids:BAQID, BAQDisplayColumn, BAQValueColumn
DropDownUserCodes - dropdown list. Information are stored in QueryCtrlValues table with one row with Id = UserCodeTypeID  */  
   ControlType:string,
      /**  Type of the datasource 0 - updatable field, 1 - parameter  */  
   SourceType:number,
      /**  ListSource  */  
   ListSource:string,
      /**  DisplayColumn  */  
   DisplayColumn:string,
      /**  ValueColumn  */  
   ValueColumn:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Seq  */  
   Seq:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_QueryCtrlValuesDesignerRow{
      /**  Company Code  */  
   Company:string,
      /**  QueryID  */  
   QueryID:string,
      /**  GUID for control  */  
   ControlID:string,
      /**  Id pof value record  */  
   ID:string,
      /**  Value  */  
   Val:string,
      /**  Sequence number  */  
   Seq:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_QueryCustomActionDesignerRow{
      /**  Company Code  */  
   Company:string,
      /**  QueryID  */  
   QueryID:string,
      /**  Action ID  */  
   ActionID:string,
      /**  Displayble text for the action  */  
   ActionLabel:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_QueryDiagramRow{
      /**  Company  */  
   Company:string,
      /**  QueryID  */  
   QueryID:string,
      /**  SubQueryID  */  
   SubQueryID:string,
      /**  Seq  */  
   Seq:number,
      /**  Data  */  
   Data:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  IsKinetic  */  
   IsKinetic:boolean,
      /**  DiagramVersion  */  
   DiagramVersion:string,
      /**  LastUpdated  */  
   LastUpdated:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_QueryDiagramTableset{
   QueryDiagram:Ice_Tablesets_QueryDiagramRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_QueryExecuteSettingDesignerRow{
      /**  Company  */  
   Company:string,
      /**  QueryID  */  
   QueryID:string,
      /**  SettingID  */  
   SettingID:string,
      /**  SettingValue  */  
   SettingValue:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_QueryFieldAttributeDesignerRow{
      /**  Company  */  
   Company:string,
      /**  QueryID  */  
   QueryID:string,
      /**  SubQueryID  */  
   SubQueryID:string,
      /**  TableID  */  
   TableID:string,
      /**  FieldName  */  
   FieldName:string,
      /**  AttributeName  */  
   AttributeName:string,
      /**  Value  */  
   Value:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Flags whether the attribute was changed by user  */  
   IsOverriden:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_QueryFieldDesignerRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  QueryID  */  
   QueryID:string,
      /**  SubQueryID  */  
   SubQueryID:string,
      /**  TableID  */  
   TableID:string,
      /**  Field Name  */  
   FieldName:string,
      /**  Sequence  */  
   Seq:number,
      /**  DBSchemaName  */  
   DBSchemaName:string,
      /**  Database Table Name  */  
   DBTableName:string,
      /**  Database Field Name  */  
   DBFieldName:string,
      /**  Data Type  */  
   DataType:string,
      /**  Description  */  
   Description:string,
      /**  External  */  
   External:boolean,
      /**  IsCalculated  */  
   IsCalculated:boolean,
      /**  Formula  */  
   Formula:string,
      /**  Field Format  */  
   FieldFormat:string,
      /**  Field Label  */  
   FieldLabel:string,
      /**  TableID to use with LikeField  */  
   LikeDataFieldTableID:string,
      /**  Like Data Field Sequence  */  
   LikeDataFieldSeq:number,
      /**  Aggregation  */  
   Aggregation:string,
      /**  IsGroupBy  */  
   IsGroupBy:boolean,
      /**  Use Like  */  
   UseLike:boolean,
      /**  Like Data Field Name  */  
   LikeDataFieldName:string,
      /**  Wheither field can be updated  */  
   Updatable:boolean,
      /**  Raise event on update  */  
   RaiseEvent:boolean,
      /**  ID of Quick Search assigned to this query field  */  
   QuickSearchID:string,
      /**  This flag tells whether this display field is used as source of distinct values for drop down list in IW  */  
   DropDown:boolean,
      /**  Initial expression for updatable field, filled on UBAQ.GetNew  */  
   UpdInitExpression:string,
      /**  Alias  */  
   Alias:string,
      /**  IsRequired  */  
   IsRequired:boolean,
      /**  IsReadOnly  */  
   IsReadOnly:boolean,
      /**  DefaultValue  */  
   DefaultValue:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   SubquerySet_Alias:string,
   SubquerySet_DataType:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_QueryFunctionCallDesignerRow{
      /**  Company  */  
   Company:string,
      /**  QueryID  */  
   QueryID:string,
      /**  SubQueryID  */  
   SubQueryID:string,
      /**  FunctionID  */  
   FunctionID:string,
      /**  ParameterName  */  
   ParameterName:string,
      /**  Seq  */  
   Seq:number,
      /**  Value  */  
   Value:string,
      /**  DataType  */  
   DataType:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_QueryGroupByDesignerRow{
      /**  Company  */  
   Company:string,
      /**  QueryID  */  
   QueryID:string,
      /**  SubQueryID  */  
   SubQueryID:string,
      /**  GroupByID  */  
   GroupByID:string,
      /**  Expression  */  
   Expression:string,
      /**  Seq  */  
   Seq:number,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_QueryParameterBindingDesignerRow{
      /**  Company  */  
   Company:string,
      /**  QueryID  */  
   QueryID:string,
      /**  ReferenceID  */  
   ReferenceID:string,
      /**  ParameterID  */  
   ParameterID:string,
      /**  MappingType  */  
   MappingType:string,
      /**  MappingValue  */  
   MappingValue:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_QueryParameterDesignerRow{
      /**  Company Code  */  
   Company:string,
      /**  QueryID  */  
   QueryID:string,
      /**  ParameterID  */  
   ParameterID:string,
      /**  Data type of the parameter  */  
   ParameterType:string,
      /**  ParameterLabel  */  
   ParameterLabel:string,
      /**  Skip condition of parameter is not set  */  
   SkipIfEmpty:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_QueryReferenceDesignerRow{
      /**  Company  */  
   Company:string,
      /**  QueryID  */  
   QueryID:string,
      /**  ReferenceID  */  
   ReferenceID:string,
      /**  ReferenceName  */  
   ReferenceName:string,
      /**  RefQueryID  */  
   RefQueryID:string,
      /**  ExecType  */  
   ExecType:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_QueryRelationDesignerRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  QueryID  */  
   QueryID:string,
      /**  SubQueryID  */  
   SubQueryID:string,
      /**  Query Relation ID  */  
   RelationID:string,
      /**  IsFK  */  
   IsFK:boolean,
      /**  ParentTableID  */  
   ParentTableID:string,
      /**  ChildTableID  */  
   ChildTableID:string,
      /**  "Outer" = outer-join, "" = inner-join  */  
   JoinType:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   OuterJoin:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_QueryRelationFieldDesignerRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  QueryID  */  
   QueryID:string,
      /**  SubQueryID  */  
   SubQueryID:string,
      /**  Query Relation ID  */  
   RelationID:string,
      /**  Sequence Number  */  
   Seq:number,
      /**  Parent Field Name  */  
   ParentFieldName:string,
      /**  ParentFieldDataType  */  
   ParentFieldDataType:string,
      /**  ParentFieldIsExpr  */  
   ParentFieldIsExpr:boolean,
      /**  Child Field Name  */  
   ChildFieldName:string,
      /**  ChildFieldDataType  */  
   ChildFieldDataType:string,
      /**  ChildFieldIsExpr  */  
   ChildFieldIsExpr:boolean,
      /**  AndOr  */  
   AndOr:string,
      /**  Neg  */  
   Neg:boolean,
      /**  LeftP  */  
   LeftP:string,
      /**  RightP  */  
   RightP:string,
      /**  CompOp  */  
   CompOp:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_QuerySortByDesignerRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  QueryID  */  
   QueryID:string,
      /**  SubQueryID  */  
   SubQueryID:string,
      /**  TableID  */  
   TableID:string,
      /**  Field Name  */  
   FieldName:string,
      /**  Sequence Number  */  
   Seq:number,
      /**  IsAsc  */  
   IsAsc:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   DisplayName:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_QuerySubQueryDesignerRow{
      /**  Company  */  
   Company:string,
      /**  QueryID  */  
   QueryID:string,
      /**  SubQueryID  */  
   SubQueryID:string,
      /**  Name  */  
   Name:string,
      /**  Type  */  
   Type:string,
      /**  Seq  */  
   Seq:number,
      /**  IsUnion  */  
   IsUnion:boolean,
      /**  LeftP  */  
   LeftP:string,
      /**  RightP  */  
   RightP:string,
      /**  SelectListClause  */  
   SelectListClause:string,
      /**  TopRowExpr  */  
   TopRowExpr:number,
      /**  TopInPercent  */  
   TopInPercent:boolean,
      /**  TopWithTies  */  
   TopWithTies:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  OrderByOffSet  */  
   OrderByOffSet:string,
      /**  OrderByFetch  */  
   OrderByFetch:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_QueryTableDesignerRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  QueryID  */  
   QueryID:string,
      /**  SubQueryID  */  
   SubQueryID:string,
      /**  TableID  */  
   TableID:string,
      /**  Sequence Number  */  
   Seq:number,
      /**  DBSchemaName  */  
   DBSchemaName:string,
      /**  Database Table Name  */  
   DBTableName:string,
      /**  TableType  */  
   TableType:string,
      /**  Summary Table flag  */  
   IsSummaryTable:boolean,
      /**  IsVisibleInDesigner  */  
   IsVisibleInDesigner:boolean,
      /**  Modifiers  */  
   Modifiers:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  PivotFunction  */  
   PivotFunction:string,
      /**  PivotDataType  */  
   PivotDataType:string,
      /**  PivotFieldFormat  */  
   PivotFieldFormat:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_QueryUpdateFieldDesignerRow{
      /**  Company Code  */  
   Company:string,
      /**  QueryID  */  
   QueryID:string,
      /**  MapTableName  */  
   MapTableName:string,
      /**  MapFieldName  */  
   MapFieldName:string,
      /**  Direction  */  
   Direction:boolean,
      /**  Expression  */  
   Expression:string,
      /**  IsKeyField  */  
   IsKeyField:boolean,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  NetDataType  */  
   NetDataType:string,
      /**  Shows field description - taken from zDataField  */  
   Description:string,
      /**  DBTableName + "." + DBFieldName  */  
   QualifiedName:string,
      /**  Shows if field is required - taken from zDataField  */  
   Required:boolean,
      /**  Shows field data type - taken from zDataField  */  
   DataType:string,
   NullableType:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_QueryUpdateSettingsDesignerRow{
      /**  Company  */  
   Company:string,
      /**  QueryID  */  
   QueryID:string,
      /**  AllowAddNew  */  
   AllowAddNew:boolean,
      /**  AddNewLabel  */  
   AddNewLabel:string,
      /**  SupportMDR  */  
   SupportMDR:boolean,
      /**  UpdatableType  */  
   UpdatableType:string,
      /**  UpdatableBO  */  
   UpdatableBO:string,
      /**  BOSystemCode  */  
   BOSystemCode:string,
      /**  UpdateMethod  */  
   UpdateMethod:string,
      /**  SCUrl  */  
   SCUrl:string,
      /**  SCWorkflow  */  
   SCWorkflow:string,
      /**  SCCtxUser  */  
   SCCtxUser:string,
      /**  SCCtxPwd  */  
   SCCtxPwd:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  SCUserID  */  
   SCUserID:string,
      /**  SCPassword  */  
   SCPassword:string,
      /**  SCCtxUrl  */  
   SCCtxUrl:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_QueryValueSetItemsDesignerRow{
      /**  Company Code  */  
   Company:string,
      /**  QueryID  */  
   QueryID:string,
      /**  ID of set of values. Is referenced by QueryWhereItem record for example.  */  
   ValueSetID:string,
      /**  Item Value  */  
   ItemValue:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_QueryWhereItemDesignerRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  QueryID  */  
   QueryID:string,
      /**  SubQueryID  */  
   SubQueryID:string,
      /**  TableID  */  
   TableID:string,
      /**  CriteriaID  */  
   CriteriaID:string,
      /**  Sequence Number  */  
   Seq:number,
   FieldName:string,
      /**  DataType  */  
   DataType:string,
      /**  Operator to use for relation between left value and right value.  */  
   CompOp:string,
   AndOr:string,
   Neg:boolean,
      /**  LeftP  */  
   LeftP:string,
      /**  RightP  */  
   RightP:string,
      /**  Indicates that the ChildField is a contant rather than a database field.  Example: Relationships to Reason requires a reasontype which would be entered as a constant.  */  
   IsConst:boolean,
      /**  CriteriaType  */  
   CriteriaType:number,
   UseHaving:boolean,
      /**  ToTableID  */  
   ToTableID:string,
   ToFieldName:string,
      /**  ToDataType  */  
   ToDataType:string,
   RValue:string,
      /**  ExtSecurity  */  
   ExtSecurity:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_QuickSearchBAQRow{
      /**  Company Identifier. If blank then this quick search is for all companies.  */  
   Company:string,
      /**  The unique identifier for this quick search  */  
   QuickSearchID:string,
   GlbCompany:string,
      /**  Description  */  
   Description:string,
      /**  The unique export identifier.  */  
   ExportID:string,
      /**  true if this search is available to all fields that have the same like table/field.  */  
   GlobalSearch:boolean,
   IsShared:boolean,
      /**  Used for indicating this quick search is provided by system, not by an end user.  */  
   SystemFlag:boolean,
      /**  Country Group Code / Country Code for CSF  */  
   CGCCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_SvcListRow{
      /**  ClassName  */  
   SvcName:string,
      /**  Description  */  
   Description:string,
   SystemCode:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_SvcListTableset{
   SvcList:Ice_Tablesets_SvcListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_TableFieldAttributeListRow{
   TableID:string,
   FieldName:string,
   AttributeName:string,
   AttributeValue:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_TableFieldListRow{
      /**  DataTable ID  */  
   DataTableID:string,
      /**  Field Name  */  
   FieldName:string,
      /**  Sequence  */  
   Seq:number,
      /**  Database Schema Name  */  
   DBSchemaName:string,
      /**  Database Table Name  */  
   DBTableName:string,
      /**  Database Field Name  */  
   DBFieldName:string,
      /**  Data Type  */  
   DataType:string,
      /**  Default Value  */  
   DefaultValue:string,
      /**  Required  */  
   Required:boolean,
      /**  Read Only  */  
   ReadOnly:boolean,
      /**  Description  */  
   Description:string,
      /**  External  */  
   External:boolean,
      /**  Formula  */  
   Formula:string,
      /**  Included  */  
   Included:boolean,
      /**  Field Format  */  
   FieldFormat:string,
      /**  Field Label  */  
   FieldLabel:string,
      /**  TableID to use with LikeField  */  
   LikeDataFieldTableID:string,
      /**  Like Data Fiel Name reference  */  
   LikeDataFieldName:string,
   IsNullable:boolean,
   CGCCode:string,
   BizType:string,
   PredictiveSearch:string,
   CurrencyCodeColumn:string,
   CurrencyType:string,
   CurrencySource:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_TableFieldListTableset{
   TableFieldList:Ice_Tablesets_TableFieldListRow[],
   TableFieldAttributeList:Ice_Tablesets_TableFieldAttributeListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_UpdExtBAQDesignerTableset{
   DynamicQueryDesigner:Ice_Tablesets_DynamicQueryDesignerRow[],
   QueryCtrlDesigner:Ice_Tablesets_QueryCtrlDesignerRow[],
   QueryCtrlValuesDesigner:Ice_Tablesets_QueryCtrlValuesDesignerRow[],
   QueryCustomActionDesigner:Ice_Tablesets_QueryCustomActionDesignerRow[],
   QueryExecuteSettingDesigner:Ice_Tablesets_QueryExecuteSettingDesignerRow[],
   QueryParameterDesigner:Ice_Tablesets_QueryParameterDesignerRow[],
   QueryReferenceDesigner:Ice_Tablesets_QueryReferenceDesignerRow[],
   QueryParameterBindingDesigner:Ice_Tablesets_QueryParameterBindingDesignerRow[],
   QuerySubQueryDesigner:Ice_Tablesets_QuerySubQueryDesignerRow[],
   QueryRelationDesigner:Ice_Tablesets_QueryRelationDesignerRow[],
   QueryRelationFieldDesigner:Ice_Tablesets_QueryRelationFieldDesignerRow[],
   QuerySortByDesigner:Ice_Tablesets_QuerySortByDesignerRow[],
   QueryWhereItemDesigner:Ice_Tablesets_QueryWhereItemDesignerRow[],
   QueryGroupByDesigner:Ice_Tablesets_QueryGroupByDesignerRow[],
   QueryTableDesigner:Ice_Tablesets_QueryTableDesignerRow[],
   QueryFieldDesigner:Ice_Tablesets_QueryFieldDesignerRow[],
   QueryFieldAttributeDesigner:Ice_Tablesets_QueryFieldAttributeDesignerRow[],
   QueryFunctionCallDesigner:Ice_Tablesets_QueryFunctionCallDesignerRow[],
   QueryUpdateFieldDesigner:Ice_Tablesets_QueryUpdateFieldDesignerRow[],
   QueryUpdateSettingsDesigner:Ice_Tablesets_QueryUpdateSettingsDesignerRow[],
   QueryValueSetItemsDesigner:Ice_Tablesets_QueryValueSetItemsDesignerRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_UsedInBAQListRow{
      /**  Company  */  
   Company:string,
      /**  QueryID  */  
   QueryID:string,
      /**  Description  */  
   Description:string,
      /**  IsGlobal  */  
   IsGlobal:boolean,
      /**  IsShared  */  
   IsShared:boolean,
      /**  CGCCode  */  
   CGCCode:string,
      /**  GlbCompany  */  
   GlbCompany:string,
      /**  ExtQuery  */  
   ExtQuery:boolean,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_UsedInBAQListTableset{
   BAQReportList:Ice_Tablesets_BAQReportListRow[],
   DashBdBAQ:Ice_Tablesets_DashBdBAQRow[],
   QuickSearchBAQ:Ice_Tablesets_QuickSearchBAQRow[],
   UsedInBAQList:Ice_Tablesets_UsedInBAQListRow[],
   UsedInReportBAQList:Ice_Tablesets_UsedInReportBAQListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_UsedInReportBAQListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Report Data Definition ID  */  
   RptDefID:string,
      /**  The Report Type similar to the one set in the Report Styles, that will help to identify which report type is this data definition intended for.  */  
   RptTypeID:string,
      /**  Country Group Code / Country Code for CSF  */  
   CGCCode:string,
      /**  Report Data Definition Description  */  
   RptDescription:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  CompanyVisibility  */  
   CompanyVisibility:number,
      /**   Indicates if this is a base system report data defintion. System report data defintions  can not be modified by users. This defintion corresponds to the base report programs (@ Crystal.rpt)
If the user requires modification they can make a duplicate and make the necessary changes to that version.  */  
   SystemRpt:boolean,
      /**  SystemFlag  */  
   SystemFlag:boolean,
   Global:boolean,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param newQueryId
      @param importBytes
      @param options
   */  
export interface ImportBaq_input{
   newQueryId:string,
   importBytes:string,
   options:any,      //schema had no properties on an object.
}

export interface ImportBaq_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   options: UNKNOW TYPE(error 2338),
   logResult:any[],
}
}

   /** Required : 
      @param ds
   */  
export interface ImportQuery_input{
   ds:Ice_Tablesets_BAQDesignerTableset[],
}

export interface ImportQuery_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_BAQDesignerTableset[],
}
}

   /** Required : 
      @param queryID
      @param companyID
   */  
export interface LoadKineticQueryDiagram_input{
      /**  The Query(QueryHdr) ID  */  
   queryID:string,
      /**  The Company) ID  */  
   companyID:string,
}

export interface LoadKineticQueryDiagram_output{
   returnObj:Ice_Tablesets_QueryDiagramTableset[],
}

   /** Required : 
      @param queryID
      @param companyID
   */  
export interface LoadQueryDiagram_input{
      /**  The Query(QueryHdr) ID  */  
   queryID:string,
      /**  The Company) ID  */  
   companyID:string,
}

export interface LoadQueryDiagram_output{
   returnObj:Ice_Tablesets_QueryDiagramTableset[],
}

   /** Required : 
      @param tableNames
   */  
export interface PossibleBONames_input{
      /**  comma delimeted table name list  */  
   tableNames:string,
}

export interface PossibleBONames_output{
parameters : {
      /**  output parameters  */  
   boNames:string,
}
}

   /** Required : 
      @param companyID
      @param queryID
   */  
export interface RegenUpdatableQueryBpm_input{
   companyID:string,
   queryID:string,
}

export interface RegenUpdatableQueryBpm_output{
}

   /** Required : 
      @param flags
   */  
export interface ResetCache_input{
      /**  Enumeration of caches to reset  */  
   flags:number,
}

export interface ResetCache_output{
}

   /** Required : 
      @param ds
   */  
export interface SaveQueryDiagram_input{
   ds:Ice_Tablesets_QueryDiagramTableset[],
}

export interface SaveQueryDiagram_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_QueryDiagramTableset[],
}
}

   /** Required : 
      @param queryId
      @param secCode
   */  
export interface SetSecurityCodeToSystemQuery_input{
      /**  Id of system query  */  
   queryId:string,
      /**  Security code  */  
   secCode:string,
}

export interface SetSecurityCodeToSystemQuery_output{
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Ice_Tablesets_UpdExtBAQDesignerTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_UpdExtBAQDesignerTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param extDsName
      @param extDsTypeName
   */  
export interface UpdateQueriesSecurityFiltersByDs_input{
      /**  ID of External Datasource or empty string if next param value is specified  */  
   extDsName:string,
      /**  ID of External Datasource Type or empty string if first param value specified  */  
   extDsTypeName:string,
}

export interface UpdateQueriesSecurityFiltersByDs_output{
}

   /** Required : 
      @param queryTableSet
   */  
export interface UpdateQuerySecurityFilters_input{
   queryTableSet:Ice_Tablesets_BAQDesignerTableset[],
}

export interface UpdateQuerySecurityFilters_output{
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Ice_Tablesets_BAQDesignerTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_BAQDesignerTableset[],
}
}

   /** Required : 
      @param queryID
      @param companyID
   */  
export interface ValidateQueryID_input{
      /**  The proposed Query ID  */  
   queryID:string,
      /**  The company where to search query  */  
   companyID:string,
}

export interface ValidateQueryID_output{
parameters : {
      /**  output parameters  */  
   foundQueryID:string,
   foundCompanyID:string,
   authorID:string,
   isShared:boolean,
   isExternal:boolean,
   isSystem:boolean,
   isGlobal:boolean,
   secCode:string,
}
}

