import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.CustomerPartXRefSvc
// Description: Customer Part Cross References BO
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/$metadata", {
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
   Description: Get CustomerPartXRefs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CustomerPartXRefs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CustXPrtRow
   */  
export function get_CustomerPartXRefs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustXPrtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/CustomerPartXRefs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustXPrtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CustomerPartXRefs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CustXPrtRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CustXPrtRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CustomerPartXRefs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/CustomerPartXRefs", {
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
   Summary: Calls GetByID to retrieve the CustomerPartXRef item
   Description: Calls GetByID to retrieve the CustomerPartXRef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CustomerPartXRef
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param XPartNum Desc: XPartNum   Required: True   Allow empty value : True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CustXPrtRow
   */  
export function get_CustomerPartXRefs_Company_CustNum_PartNum_XPartNum_SysRowID(Company:string, CustNum:string, PartNum:string, XPartNum:string, SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CustXPrtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/CustomerPartXRefs(" + Company + "," + CustNum + "," + PartNum + "," + XPartNum + "," + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CustXPrtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CustomerPartXRef for the service
   Description: Calls UpdateExt to update CustomerPartXRef. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CustomerPartXRef
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param XPartNum Desc: XPartNum   Required: True   Allow empty value : True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CustXPrtRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CustomerPartXRefs_Company_CustNum_PartNum_XPartNum_SysRowID(Company:string, CustNum:string, PartNum:string, XPartNum:string, SysRowID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/CustomerPartXRefs(" + Company + "," + CustNum + "," + PartNum + "," + XPartNum + "," + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete CustomerPartXRef item
   Description: Call UpdateExt to delete CustomerPartXRef item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CustomerPartXRef
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param XPartNum Desc: XPartNum   Required: True   Allow empty value : True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CustomerPartXRefs_Company_CustNum_PartNum_XPartNum_SysRowID(Company:string, CustNum:string, PartNum:string, XPartNum:string, SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/CustomerPartXRefs(" + Company + "," + CustNum + "," + PartNum + "," + XPartNum + "," + SysRowID + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CustXPrtListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustXPrtListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustXPrtListRow)
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
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseCustXPrt:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseCustXPrt!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCustXPrt=" + whereClauseCustXPrt
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/GetRows" + params, {
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
   Required: True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(custNum:string, partNum:string, xpartNum:string, sysRowID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof custNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "custNum=" + custNum
   }
   if(typeof partNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "partNum=" + partNum
   }
   if(typeof xpartNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "xpartNum=" + xpartNum
   }
   if(typeof sysRowID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "sysRowID=" + sysRowID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/GetList" + params, {
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
   Summary: Invoke method ChangeCustXPrtPartNum
   Description: When Changing CustXPrt.PartNum field.
   OperationID: ChangeCustXPrtPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCustXPrtPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCustXPrtPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCustXPrtPartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/ChangeCustXPrtPartNum", {
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
   Summary: Invoke method ChangeListCustXPrtPartNum
   Description: When Changing CustXPrtList.PartNum field.
   OperationID: ChangeListCustXPrtPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeListCustXPrtPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeListCustXPrtPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeListCustXPrtPartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/ChangeListCustXPrtPartNum", {
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
   Summary: Invoke method ChangeCustXPrtSNMask
   Description: When Changing CustXPrt.SNMask field.
   OperationID: ChangeCustXPrtSNMask
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCustXPrtSNMask_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCustXPrtSNMask_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCustXPrtSNMask(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/ChangeCustXPrtSNMask", {
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
   Summary: Invoke method ChangeCustXPrtSNOverride
   Description: When Changing PartRef.SNOverride field.
   OperationID: ChangeCustXPrtSNOverride
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCustXPrtSNOverride_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCustXPrtSNOverride_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCustXPrtSNOverride(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/ChangeCustXPrtSNOverride", {
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
   Summary: Invoke method ChangeCustXPrtXPartNum
   Description: When Changing CustXPrt.XPartNum field.
   OperationID: ChangeCustXPrtXPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCustXPrtXPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCustXPrtXPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCustXPrtXPartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/ChangeCustXPrtXPartNum", {
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
   Summary: Invoke method IsCustXPrtXPartNumInvalid
   Description: when Changing Customer Part Num
   OperationID: IsCustXPrtXPartNumInvalid
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsCustXPrtXPartNumInvalid_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsCustXPrtXPartNumInvalid_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsCustXPrtXPartNumInvalid(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/IsCustXPrtXPartNumInvalid", {
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
   Summary: Invoke method ChangeMaskPrefixSuffix
   Description: When Changing CustomerRef.MaskPrefix or Suffix field.
   OperationID: ChangeMaskPrefixSuffix
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeMaskPrefixSuffix_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMaskPrefixSuffix_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeMaskPrefixSuffix(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/ChangeMaskPrefixSuffix", {
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
   Summary: Invoke method GetCustomerParXRef
   Description: Get all Customer Part References for a given Customer
   OperationID: GetCustomerParXRef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCustomerParXRef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCustomerParXRef_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCustomerParXRef(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/GetCustomerParXRef", {
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
   Summary: Invoke method FindCustPartNum
   Description: Find Customer Part Number.
   OperationID: FindCustPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FindCustPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindCustPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FindCustPartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/FindCustPartNum", {
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
   Summary: Invoke method GetCustPartXCustPartRef
   Description: Get Customer Part Cross References for a given Customer and PartNum
   OperationID: GetCustPartXCustPartRef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCustPartXCustPartRef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCustPartXCustPartRef_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCustPartXCustPartRef(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/GetCustPartXCustPartRef", {
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
   Summary: Invoke method GetListCustPartXCustPartRef
   Description: Get Customer Part Cross References List for a given Customer and PartNum
   OperationID: GetListCustPartXCustPartRef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListCustPartXCustPartRef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListCustPartXCustPartRef_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListCustPartXCustPartRef(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/GetListCustPartXCustPartRef", {
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
   Summary: Invoke method GetListCustPartXCustPartRefByID
   Description: Get Customer Part Cross References List for a List of GUIDs
   OperationID: GetListCustPartXCustPartRefByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListCustPartXCustPartRefByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListCustPartXCustPartRefByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListCustPartXCustPartRefByID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/GetListCustPartXCustPartRefByID", {
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
   Summary: Invoke method UpdateCustPartOpts
   Description: Update Customer CustPartOpts
   OperationID: UpdateCustPartOpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateCustPartOpts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateCustPartOpts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateCustPartOpts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/UpdateCustPartOpts", {
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
   Summary: Invoke method DeleteByPart
   OperationID: DeleteByPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteByPart(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/DeleteByPart", {
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
   Summary: Invoke method GetNewCustXPrt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCustXPrt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCustXPrt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCustXPrt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCustXPrt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/GetNewCustXPrt", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/UpdateExt", {
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



//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustXPrtListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CustXPrtListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustXPrtRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CustXPrtRow[],
}

export interface Erp_Tablesets_CustXPrtListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Our Part number used to identify this part.  */  
   "PartNum":string,
      /**  Contains the Customer number of this part cross reference record  */  
   "CustNum":number,
      /**  Part Number that the customer uses to identify the Part.  */  
   "XPartNum":string,
      /**  Customers Part Revision Number.  */  
   "XRevisionNum":string,
      /**  Description Customer uses to describes the Part.  */  
   "PartDescription":string,
      /**  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  */  
   "SourceDBRecid":string,
      /**  The part number used to identify the configured part number initially entered on the line.  */  
   "BasePartNum":string,
      /**  The revision number used to identify the configured part/revision number initially entered on the line.  */  
   "BaseRevisionNum":string,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  */  
   "SNMask":string,
      /**  BL-generated example of the serial number mask if SNBaseDataType = Mask.  */  
   "SNMaskExample":string,
      /**  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  */  
   "SNMaskSuffix":string,
      /**  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  */  
   "SNMaskPrefix":string,
      /**  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  */  
   "SNLastUsedSeq":string,
      /**  Override serial mask settings? SN fields are ignored unless this is true.  */  
   "SNOverride":boolean,
      /**  Marks this CustXPrt as global, available to be sent out to other companies.  */  
   "GlobalCustXPrt":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  WIApplication  */  
   "WIApplication":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  EDIContainerType  */  
   "EDIContainerType":string,
      /**  ProductionPartNum  */  
   "ProductionPartNum":string,
      /**  ProductionPartNumIsValid  */  
   "ProductionPartNumIsValid":boolean,
      /**  ServicePartNum  */  
   "ServicePartNum":string,
      /**  ServicePartNumIsValid  */  
   "ServicePartNumIsValid":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CustXPrtRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Our Part number used to identify this part.  */  
   "PartNum":string,
      /**  Contains the Customer number of this part cross reference record  */  
   "CustNum":number,
      /**  Part Number that the customer uses to identify the Part.  */  
   "XPartNum":string,
      /**  Customers Part Revision Number.  */  
   "XRevisionNum":string,
      /**  Description Customer uses to describes the Part.  */  
   "PartDescription":string,
      /**  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  */  
   "SourceDBRecid":string,
      /**  The part number used to identify the configured part number initially entered on the line.  */  
   "BasePartNum":string,
      /**  The revision number used to identify the configured part/revision number initially entered on the line.  */  
   "BaseRevisionNum":string,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  */  
   "SNMask":string,
      /**  BL-generated example of the serial number mask if SNBaseDataType = Mask.  */  
   "SNMaskExample":string,
      /**  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  */  
   "SNMaskSuffix":string,
      /**  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  */  
   "SNMaskPrefix":string,
      /**  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  */  
   "SNLastUsedSeq":string,
      /**  Override serial mask settings? SN fields are ignored unless this is true.  */  
   "SNOverride":boolean,
      /**  Marks this CustXPrt as global, available to be sent out to other companies.  */  
   "GlobalCustXPrt":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  WIApplication  */  
   "WIApplication":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  EDIContainerType  */  
   "EDIContainerType":string,
      /**  ProductionPartNum  */  
   "ProductionPartNum":string,
      /**  ProductionPartNumIsValid  */  
   "ProductionPartNumIsValid":boolean,
      /**  ServicePartNum  */  
   "ServicePartNum":string,
      /**  ServicePartNumIsValid  */  
   "ServicePartNumIsValid":boolean,
      /**  Prefix + Example + Suffix  */  
   "SNPrefixExampleSuffix":string,
      /**  SuffixLength  */  
   "SuffixLength":number,
      /**  PrefixLength  */  
   "PrefixLength":number,
   "BitFlag":number,
   "CustNumName":string,
   "CustNumBTName":string,
   "CustNumCustID":string,
   "PartSalesUM":string,
   "PartIUM":string,
   "PartPartDescription":string,
   "PartSellingFactor":number,
   "PartTrackLots":boolean,
   "PartTrackDimension":boolean,
   "PartPricePerCode":string,
   "PartTrackSerialNum":boolean,
   "SerialMaskDescription":string,
   "SerialMaskMaskType":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param iPartNum
      @param ds
      @param sysRowID
      @param rowType
   */  
export interface ChangeCustXPrtPartNum_input{
      /**  Part Number  */  
   iPartNum:string,
   ds:Erp_Tablesets_CustomerPartXRefTableset[],
      /**  RowID of the selected record. Skips find part logic if this has a value.  */  
   sysRowID:string,
      /**  RowType of the selected record. Only used with sysRowID.  */  
   rowType:string,
}

export interface ChangeCustXPrtPartNum_output{
parameters : {
      /**  output parameters  */  
   iPartNum:string,
   ds:Erp_Tablesets_CustomerPartXRefTableset[],
   serialWarning:string,
   questionString:string,
   multipleMatch:boolean,
}
}

   /** Required : 
      @param iSNMask
      @param ds
   */  
export interface ChangeCustXPrtSNMask_input{
      /**  Serial Number Mask Id  */  
   iSNMask:string,
   ds:Erp_Tablesets_CustomerPartXRefTableset[],
}

export interface ChangeCustXPrtSNMask_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustomerPartXRefTableset[],
}
}

   /** Required : 
      @param iSNOverride
      @param ds
   */  
export interface ChangeCustXPrtSNOverride_input{
      /**  Override Mask  */  
   iSNOverride:string,
   ds:Erp_Tablesets_CustomerPartXRefTableset[],
}

export interface ChangeCustXPrtSNOverride_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustomerPartXRefTableset[],
}
}

   /** Required : 
      @param iXPartNum
      @param ds
   */  
export interface ChangeCustXPrtXPartNum_input{
      /**  Customer Part Number  */  
   iXPartNum:string,
   ds:Erp_Tablesets_CustomerPartXRefTableset[],
}

export interface ChangeCustXPrtXPartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustomerPartXRefTableset[],
}
}

   /** Required : 
      @param iPartNum
      @param ds
      @param sysRowID
      @param rowType
   */  
export interface ChangeListCustXPrtPartNum_input{
   iPartNum:string,
   ds:Erp_Tablesets_CustomerPartXRefListTableset[],
   sysRowID:string,
   rowType:string,
}

export interface ChangeListCustXPrtPartNum_output{
parameters : {
      /**  output parameters  */  
   iPartNum:string,
   ds:Erp_Tablesets_CustomerPartXRefListTableset[],
   multipleMatch:boolean,
}
}

   /** Required : 
      @param icValue
      @param icPorC
      @param ds
   */  
export interface ChangeMaskPrefixSuffix_input{
      /**  MaskPrefix or MaskSuffix value  */  
   icValue:string,
      /**  Which one to check  */  
   icPorC:string,
   ds:Erp_Tablesets_CustomerPartXRefTableset[],
}

export interface ChangeMaskPrefixSuffix_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustomerPartXRefTableset[],
}
}

   /** Required : 
      @param custNum
      @param partNum
      @param xpartNum
      @param sysRowID
   */  
export interface DeleteByID_input{
   custNum:number,
   partNum:string,
   xpartNum:string,
   sysRowID:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param partNum
   */  
export interface DeleteByPart_input{
   partNum:string,
}

export interface DeleteByPart_output{
}

export interface Erp_Tablesets_CustXPrtListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Our Part number used to identify this part.  */  
   PartNum:string,
      /**  Contains the Customer number of this part cross reference record  */  
   CustNum:number,
      /**  Part Number that the customer uses to identify the Part.  */  
   XPartNum:string,
      /**  Customers Part Revision Number.  */  
   XRevisionNum:string,
      /**  Description Customer uses to describes the Part.  */  
   PartDescription:string,
      /**  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  */  
   SourceDBRecid:string,
      /**  The part number used to identify the configured part number initially entered on the line.  */  
   BasePartNum:string,
      /**  The revision number used to identify the configured part/revision number initially entered on the line.  */  
   BaseRevisionNum:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  */  
   SNMask:string,
      /**  BL-generated example of the serial number mask if SNBaseDataType = Mask.  */  
   SNMaskExample:string,
      /**  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  */  
   SNMaskSuffix:string,
      /**  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  */  
   SNMaskPrefix:string,
      /**  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  */  
   SNLastUsedSeq:string,
      /**  Override serial mask settings? SN fields are ignored unless this is true.  */  
   SNOverride:boolean,
      /**  Marks this CustXPrt as global, available to be sent out to other companies.  */  
   GlobalCustXPrt:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  WIApplication  */  
   WIApplication:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  EDIContainerType  */  
   EDIContainerType:string,
      /**  ProductionPartNum  */  
   ProductionPartNum:string,
      /**  ProductionPartNumIsValid  */  
   ProductionPartNumIsValid:boolean,
      /**  ServicePartNum  */  
   ServicePartNum:string,
      /**  ServicePartNumIsValid  */  
   ServicePartNumIsValid:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CustXPrtRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Our Part number used to identify this part.  */  
   PartNum:string,
      /**  Contains the Customer number of this part cross reference record  */  
   CustNum:number,
      /**  Part Number that the customer uses to identify the Part.  */  
   XPartNum:string,
      /**  Customers Part Revision Number.  */  
   XRevisionNum:string,
      /**  Description Customer uses to describes the Part.  */  
   PartDescription:string,
      /**  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  */  
   SourceDBRecid:string,
      /**  The part number used to identify the configured part number initially entered on the line.  */  
   BasePartNum:string,
      /**  The revision number used to identify the configured part/revision number initially entered on the line.  */  
   BaseRevisionNum:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  */  
   SNMask:string,
      /**  BL-generated example of the serial number mask if SNBaseDataType = Mask.  */  
   SNMaskExample:string,
      /**  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  */  
   SNMaskSuffix:string,
      /**  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  */  
   SNMaskPrefix:string,
      /**  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  */  
   SNLastUsedSeq:string,
      /**  Override serial mask settings? SN fields are ignored unless this is true.  */  
   SNOverride:boolean,
      /**  Marks this CustXPrt as global, available to be sent out to other companies.  */  
   GlobalCustXPrt:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  WIApplication  */  
   WIApplication:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  EDIContainerType  */  
   EDIContainerType:string,
      /**  ProductionPartNum  */  
   ProductionPartNum:string,
      /**  ProductionPartNumIsValid  */  
   ProductionPartNumIsValid:boolean,
      /**  ServicePartNum  */  
   ServicePartNum:string,
      /**  ServicePartNumIsValid  */  
   ServicePartNumIsValid:boolean,
      /**  Prefix + Example + Suffix  */  
   SNPrefixExampleSuffix:string,
      /**  SuffixLength  */  
   SuffixLength:number,
      /**  PrefixLength  */  
   PrefixLength:number,
   BitFlag:number,
   CustNumName:string,
   CustNumBTName:string,
   CustNumCustID:string,
   PartSalesUM:string,
   PartIUM:string,
   PartPartDescription:string,
   PartSellingFactor:number,
   PartTrackLots:boolean,
   PartTrackDimension:boolean,
   PartPricePerCode:string,
   PartTrackSerialNum:boolean,
   SerialMaskDescription:string,
   SerialMaskMaskType:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CustomerPartXRefListTableset{
   CustXPrtList:Erp_Tablesets_CustXPrtListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CustomerPartXRefTableset{
   CustXPrt:Erp_Tablesets_CustXPrtRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtCustomerPartXRefTableset{
   CustXPrt:Erp_Tablesets_CustXPrtRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param iCustNum
      @param partNum
      @param ds
   */  
export interface FindCustPartNum_input{
   iCustNum:number,
   partNum:string,
   ds:Erp_Tablesets_CustomerPartXRefTableset[],
}

export interface FindCustPartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustomerPartXRefTableset[],
   part:string,
   multipleMatch:boolean,
}
}

   /** Required : 
      @param custNum
      @param partNum
      @param xpartNum
      @param sysRowID
   */  
export interface GetByID_input{
   custNum:number,
   partNum:string,
   xpartNum:string,
   sysRowID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_CustomerPartXRefTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_CustomerPartXRefTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_CustomerPartXRefTableset[],
}

   /** Required : 
      @param iCustNum
      @param partNum
      @param ds
   */  
export interface GetCustPartXCustPartRef_input{
      /**  Customer Number  */  
   iCustNum:number,
      /**  Part Number  */  
   partNum:string,
   ds:Erp_Tablesets_CustomerPartXRefTableset[],
}

export interface GetCustPartXCustPartRef_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustomerPartXRefTableset[],
}
}

   /** Required : 
      @param iCustNum
      @param ds
   */  
export interface GetCustomerParXRef_input{
      /**  Customer Number  */  
   iCustNum:number,
   ds:Erp_Tablesets_CustomerPartXRefTableset[],
}

export interface GetCustomerParXRef_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustomerPartXRefTableset[],
}
}

   /** Required : 
      @param CustNum
      @param CustXPrtRowID
      @param ds
   */  
export interface GetListCustPartXCustPartRefByID_input{
   CustNum:number,
      /**  Customer Part Numbers  */  
   CustXPrtRowID:string,
   ds:Erp_Tablesets_CustomerPartXRefListTableset[],
}

export interface GetListCustPartXCustPartRefByID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustomerPartXRefListTableset[],
}
}

   /** Required : 
      @param iCustNum
      @param partNum
      @param ds
   */  
export interface GetListCustPartXCustPartRef_input{
      /**  Customer Number  */  
   iCustNum:number,
      /**  Part Number  */  
   partNum:string,
   ds:Erp_Tablesets_CustomerPartXRefListTableset[],
}

export interface GetListCustPartXCustPartRef_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustomerPartXRefListTableset[],
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
   returnObj:Erp_Tablesets_CustomerPartXRefListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param custNum
      @param partNum
      @param xpartNum
   */  
export interface GetNewCustXPrt_input{
   ds:Erp_Tablesets_CustomerPartXRefTableset[],
   custNum:number,
   partNum:string,
   xpartNum:string,
}

export interface GetNewCustXPrt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustomerPartXRefTableset[],
}
}

   /** Required : 
      @param whereClauseCustXPrt
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseCustXPrt:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_CustomerPartXRefTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
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

   /** Required : 
      @param iXPartNum
      @param custNum
   */  
export interface IsCustXPrtXPartNumInvalid_input{
   iXPartNum:string,
   custNum:number,
}

export interface IsCustXPrtXPartNumInvalid_output{
   returnObj:boolean,
}

   /** Required : 
      @param pcCustID
      @param pcCustPartOpts
   */  
export interface UpdateCustPartOpts_input{
      /**  CustID  */  
   pcCustID:string,
      /**  CustPartOpts  */  
   pcCustPartOpts:string,
}

export interface UpdateCustPartOpts_output{
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtCustomerPartXRefTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtCustomerPartXRefTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_CustomerPartXRefTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustomerPartXRefTableset[],
}
}

