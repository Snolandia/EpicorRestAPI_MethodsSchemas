import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.Form1099Svc
// Description: 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/$metadata", {
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
   Description: Get Form1099s items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Form1099s
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.Form1099Row
   */  
export function get_Form1099s(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_Form1099Row>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/Form1099s", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_Form1099Row)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Form1099s
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.Form1099Row
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.Form1099Row
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Form1099s(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/Form1099s", {
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
   Summary: Calls GetByID to retrieve the Form1099 item
   Description: Calls GetByID to retrieve the Form1099 item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Form1099
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param FormTypeID Desc: FormTypeID   Required: True   Allow empty value : True
      @param Form1099Num Desc: Form1099Num   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.Form1099Row
   */  
export function get_Form1099s_Company_FormTypeID_Form1099Num(Company:string, FormTypeID:string, Form1099Num:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_Form1099Row>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/Form1099s(" + Company + "," + FormTypeID + "," + Form1099Num + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_Form1099Row)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update Form1099 for the service
   Description: Calls UpdateExt to update Form1099. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Form1099
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param FormTypeID Desc: FormTypeID   Required: True   Allow empty value : True
      @param Form1099Num Desc: Form1099Num   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.Form1099Row
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_Form1099s_Company_FormTypeID_Form1099Num(Company:string, FormTypeID:string, Form1099Num:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/Form1099s(" + Company + "," + FormTypeID + "," + Form1099Num + ")", {
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
   Summary: Call UpdateExt to delete Form1099 item
   Description: Call UpdateExt to delete Form1099 item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Form1099
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param FormTypeID Desc: FormTypeID   Required: True   Allow empty value : True
      @param Form1099Num Desc: Form1099Num   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_Form1099s_Company_FormTypeID_Form1099Num(Company:string, FormTypeID:string, Form1099Num:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/Form1099s(" + Company + "," + FormTypeID + "," + Form1099Num + ")", {
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
   Description: Get Form1099Dtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_Form1099Dtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param FormTypeID Desc: FormTypeID   Required: True   Allow empty value : True
      @param Form1099Num Desc: Form1099Num   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.Form1099DtlRow
   */  
export function get_Form1099s_Company_FormTypeID_Form1099Num_Form1099Dtls(Company:string, FormTypeID:string, Form1099Num:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_Form1099DtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/Form1099s(" + Company + "," + FormTypeID + "," + Form1099Num + ")/Form1099Dtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_Form1099DtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the Form1099Dtl item
   Description: Calls GetByID to retrieve the Form1099Dtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Form1099Dtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param FormTypeID Desc: FormTypeID   Required: True   Allow empty value : True
      @param Form1099Num Desc: Form1099Num   Required: True
      @param Code1099ID Desc: Code1099ID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.Form1099DtlRow
   */  
export function get_Form1099s_Company_FormTypeID_Form1099Num_Form1099Dtls_Company_FormTypeID_Form1099Num_Code1099ID(Company:string, FormTypeID:string, Form1099Num:string, Code1099ID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_Form1099DtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/Form1099s(" + Company + "," + FormTypeID + "," + Form1099Num + ")/Form1099Dtls(" + Company + "," + FormTypeID + "," + Form1099Num + "," + Code1099ID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_Form1099DtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get Form1099Dtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Form1099Dtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.Form1099DtlRow
   */  
export function get_Form1099Dtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_Form1099DtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/Form1099Dtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_Form1099DtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Form1099Dtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.Form1099DtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.Form1099DtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Form1099Dtls(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/Form1099Dtls", {
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
   Summary: Calls GetByID to retrieve the Form1099Dtl item
   Description: Calls GetByID to retrieve the Form1099Dtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Form1099Dtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param FormTypeID Desc: FormTypeID   Required: True   Allow empty value : True
      @param Form1099Num Desc: Form1099Num   Required: True
      @param Code1099ID Desc: Code1099ID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.Form1099DtlRow
   */  
export function get_Form1099Dtls_Company_FormTypeID_Form1099Num_Code1099ID(Company:string, FormTypeID:string, Form1099Num:string, Code1099ID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_Form1099DtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/Form1099Dtls(" + Company + "," + FormTypeID + "," + Form1099Num + "," + Code1099ID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_Form1099DtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update Form1099Dtl for the service
   Description: Calls UpdateExt to update Form1099Dtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Form1099Dtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param FormTypeID Desc: FormTypeID   Required: True   Allow empty value : True
      @param Form1099Num Desc: Form1099Num   Required: True
      @param Code1099ID Desc: Code1099ID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.Form1099DtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_Form1099Dtls_Company_FormTypeID_Form1099Num_Code1099ID(Company:string, FormTypeID:string, Form1099Num:string, Code1099ID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/Form1099Dtls(" + Company + "," + FormTypeID + "," + Form1099Num + "," + Code1099ID + ")", {
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
   Summary: Call UpdateExt to delete Form1099Dtl item
   Description: Call UpdateExt to delete Form1099Dtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Form1099Dtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param FormTypeID Desc: FormTypeID   Required: True   Allow empty value : True
      @param Form1099Num Desc: Form1099Num   Required: True
      @param Code1099ID Desc: Code1099ID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_Form1099Dtls_Company_FormTypeID_Form1099Num_Code1099ID(Company:string, FormTypeID:string, Form1099Num:string, Code1099ID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/Form1099Dtls(" + Company + "," + FormTypeID + "," + Form1099Num + "," + Code1099ID + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.Form1099ListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_Form1099ListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_Form1099ListRow)
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
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseForm1099:string, whereClauseForm1099Dtl:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseForm1099!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseForm1099=" + whereClauseForm1099
   }
   if(typeof whereClauseForm1099Dtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseForm1099Dtl=" + whereClauseForm1099Dtl
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/GetRows" + params, {
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
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(formTypeID:string, form1099Num:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof formTypeID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "formTypeID=" + formTypeID
   }
   if(typeof form1099Num!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "form1099Num=" + form1099Num
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/GetList" + params, {
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
   Summary: Invoke method OnChange1099Code
   Description: Call this method when the user enters the Form1099Dtl.Code1099ID
   OperationID: OnChange1099Code
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChange1099Code_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChange1099Code_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChange1099Code(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/OnChange1099Code", {
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
   Summary: Invoke method OnChangeBoxAmount
   Description: Call this method when the user enters the Form1099Dtl.BoxAmt
   OperationID: OnChangeBoxAmount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeBoxAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBoxAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeBoxAmount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/OnChangeBoxAmount", {
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
   Summary: Invoke method OnChangeBoxNum
   Description: Call this method when the user enters the ttForm1099Dtl.BoxNum
   OperationID: OnChangeBoxNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeBoxNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBoxNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeBoxNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/OnChangeBoxNum", {
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
   Summary: Invoke method OnChangeVendor
   Description: Call this method when the user enters the ttForm1099.VendorID
   OperationID: OnChangeVendor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeVendor(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/OnChangeVendor", {
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
   Summary: Invoke method Void1099Form
   Description: Void 1099 Form by Action Menu from UI
   OperationID: Void1099Form
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Void1099Form_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Void1099Form_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Void1099Form(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/Void1099Form", {
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
   Summary: Invoke method ValidateUpdate
   Description: Validate the record was updated
   OperationID: ValidateUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateUpdate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/ValidateUpdate", {
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
   Summary: Invoke method GetDefaultFormType
   Description: Obtain Default value for 1099 Form Type combo
   OperationID: GetDefaultFormType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultFormType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDefaultFormType(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/GetDefaultFormType", {
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
   Summary: Invoke method ValidateFormTypeID
   Description: Returns a description of the entered 1099 Form Type
   OperationID: ValidateFormTypeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateFormTypeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateFormTypeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateFormTypeID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/ValidateFormTypeID", {
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
   Summary: Invoke method CheckFormTypeID
   Description: Checks 1099 Form Type entered
   OperationID: CheckFormTypeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckFormTypeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckFormTypeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckFormTypeID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/CheckFormTypeID", {
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
   Summary: Invoke method GetByIDSite
   OperationID: GetByIDSite
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByIDSite_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDSite_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByIDSite(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/GetByIDSite", {
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
   Summary: Invoke method GetNewForm1099
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewForm1099
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewForm1099_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewForm1099_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewForm1099(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/GetNewForm1099", {
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
   Summary: Invoke method GetNewForm1099Dtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewForm1099Dtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewForm1099Dtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewForm1099Dtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewForm1099Dtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/GetNewForm1099Dtl", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_Form1099DtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_Form1099DtlRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_Form1099ListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_Form1099ListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_Form1099Row{
   "odatametadata":string,
   "value":Erp_Tablesets_Form1099Row[],
}

export interface Erp_Tablesets_Form1099DtlRow{
      /**  Company identifier  */  
   "Company":string,
      /**  Form Type ID  */  
   "FormTypeID":string,
      /**  1099 Form Number  */  
   "Form1099Num":number,
      /**  1099 Code  */  
   "Code1099ID":string,
      /**  Box Amount  */  
   "BoxAmt":number,
      /**  Box Number  */  
   "BoxNum":string,
      /**  Box Number Description  */  
   "BoxNumDesc":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
   "Code1099Description":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_Form1099ListRow{
      /**  Company identifier  */  
   "Company":string,
      /**  Form Type ID  */  
   "FormTypeID":string,
      /**  1099 Form Number  */  
   "Form1099Num":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_Form1099Row{
      /**  Company identifier  */  
   "Company":string,
      /**  Form Type ID  */  
   "FormTypeID":string,
      /**  1099 Form Number  */  
   "Form1099Num":number,
      /**  Comment  */  
   "Comment":string,
      /**  First address line of the Supplier Address  */  
   "Address1":string,
      /**  Second address line of the Supplier Address  */  
   "Address2":string,
      /**  Third address line of the Supplier Address  */  
   "Address3":string,
      /**  Supplier City  */  
   "City":string,
      /**  Supplier State  */  
   "State":string,
      /**  Supplier Postal Code  */  
   "ZIP":string,
      /**  County Number for Non US Suppliers  */  
   "CountryNum":number,
      /**  Country Name  */  
   "Country":string,
      /**  Second TIN Notice  */  
   "SecondTINNotice":boolean,
      /**  Corrected  */  
   "Corrected":boolean,
      /**  2 Step Correction  */  
   "TwoStepCorrection":boolean,
      /**  User Modified  */  
   "UserModified":boolean,
      /**  Void  */  
   "Void":boolean,
      /**  Printed  */  
   "Printed":boolean,
      /**  Submitted  */  
   "Submitted":boolean,
      /**  Indicates that the form was submitted  electronically  */  
   "SubmittedElectronic":boolean,
      /**  Date submitted electronically  */  
   "ElectronicDate":string,
      /**  Payment Year  */  
   "PaymentYear":number,
      /**  TIN Type. Values are 1 for EIN, 2 for SSNs, ITINs, and ATINs and 0 if type of TIN is not terminable.  */  
   "TINType":string,
      /**  Correction of, it is an existing 1099 Form Number which was already generated for selected year/supplier or TIN/TYPE.  */  
   "CorrectionOf":number,
      /**  Supplier Number  */  
   "VendorNum":number,
      /**  Corrected By  */  
   "CorrectedBy":number,
      /**  First line of the Supplier Name  */  
   "Name1":string,
      /**  Second line of the Supplier Name  */  
   "Name2":string,
      /**  Name Control, optional and used for electronic export  */  
   "NameControl":string,
      /**  Payee Account Number  */  
   "AccountNum":string,
      /**  Supplier TIN  */  
   "TIN":string,
      /**  Ttime submitted electronically  */  
   "TimeSubmitted":number,
      /**  Generation Date  */  
   "GenDate":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  Non US Supplier  */  
   "NonUS":boolean,
      /**  FATCA  */  
   "FATCA":boolean,
      /**  Form 1099-K Transaction Type  */  
   "US1099KTranType":string,
      /**  Form 1099-K Merchant Category Code  */  
   "US1099KMerchCatCode":string,
      /**  Plant  */  
   "Plant":string,
      /**  Company Address  */  
   "CompanyAddress":string,
      /**  Company Address 2nd Line  */  
   "CompanyAddress2":string,
      /**  Company Address 3rd Line  */  
   "CompanyAddress3":string,
      /**  City portion of company address  */  
   "CompanyCity":string,
      /**  Company Name  */  
   "CompanyName":string,
      /**  Company Name 2nd Line  */  
   "CompanyName2":string,
      /**  State portion of company address  */  
   "CompanyState":string,
      /**  Company TIN  */  
   "CompanyTIN":string,
      /**  Postal code or zip code portion of company address.  */  
   "CompanyZIP":string,
      /**  Company phone number  */  
   "CountryPhone":string,
      /**  Check field to determine wheter the record was modified by the user or not.  */  
   "ModifiedAndSaved":boolean,
   "BitFlag":number,
   "FormTypeDescription":string,
   "VendorVendorNum":number,
   "VendorNonUS":boolean,
   "VendorAddress1":string,
   "VendorCity":string,
   "VendorAccountNum":string,
   "VendorAddress2":string,
   "VendorVendorID":string,
   "VendorNameControl":string,
   "VendorZIP":string,
   "VendorReporting1099Name":string,
   "VendorAddress3":string,
   "VendorState":string,
   "VendorCountryNum":number,
   "VendorFATCA":boolean,
   "VendorReporting1099Name2":string,
   "VendorSecondTINNotice":boolean,
   "VendorTINType":string,
   "VendorTIN":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param newFormTypeID
   */  
export interface CheckFormTypeID_input{
   newFormTypeID:string,
}

export interface CheckFormTypeID_output{
}

   /** Required : 
      @param formTypeID
      @param form1099Num
   */  
export interface DeleteByID_input{
   formTypeID:string,
   form1099Num:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_Form1099DtlRow{
      /**  Company identifier  */  
   Company:string,
      /**  Form Type ID  */  
   FormTypeID:string,
      /**  1099 Form Number  */  
   Form1099Num:number,
      /**  1099 Code  */  
   Code1099ID:string,
      /**  Box Amount  */  
   BoxAmt:number,
      /**  Box Number  */  
   BoxNum:string,
      /**  Box Number Description  */  
   BoxNumDesc:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
   Code1099Description:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_Form1099ListRow{
      /**  Company identifier  */  
   Company:string,
      /**  Form Type ID  */  
   FormTypeID:string,
      /**  1099 Form Number  */  
   Form1099Num:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_Form1099ListTableset{
   Form1099List:Erp_Tablesets_Form1099ListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_Form1099Row{
      /**  Company identifier  */  
   Company:string,
      /**  Form Type ID  */  
   FormTypeID:string,
      /**  1099 Form Number  */  
   Form1099Num:number,
      /**  Comment  */  
   Comment:string,
      /**  First address line of the Supplier Address  */  
   Address1:string,
      /**  Second address line of the Supplier Address  */  
   Address2:string,
      /**  Third address line of the Supplier Address  */  
   Address3:string,
      /**  Supplier City  */  
   City:string,
      /**  Supplier State  */  
   State:string,
      /**  Supplier Postal Code  */  
   ZIP:string,
      /**  County Number for Non US Suppliers  */  
   CountryNum:number,
      /**  Country Name  */  
   Country:string,
      /**  Second TIN Notice  */  
   SecondTINNotice:boolean,
      /**  Corrected  */  
   Corrected:boolean,
      /**  2 Step Correction  */  
   TwoStepCorrection:boolean,
      /**  User Modified  */  
   UserModified:boolean,
      /**  Void  */  
   Void:boolean,
      /**  Printed  */  
   Printed:boolean,
      /**  Submitted  */  
   Submitted:boolean,
      /**  Indicates that the form was submitted  electronically  */  
   SubmittedElectronic:boolean,
      /**  Date submitted electronically  */  
   ElectronicDate:string,
      /**  Payment Year  */  
   PaymentYear:number,
      /**  TIN Type. Values are 1 for EIN, 2 for SSNs, ITINs, and ATINs and 0 if type of TIN is not terminable.  */  
   TINType:string,
      /**  Correction of, it is an existing 1099 Form Number which was already generated for selected year/supplier or TIN/TYPE.  */  
   CorrectionOf:number,
      /**  Supplier Number  */  
   VendorNum:number,
      /**  Corrected By  */  
   CorrectedBy:number,
      /**  First line of the Supplier Name  */  
   Name1:string,
      /**  Second line of the Supplier Name  */  
   Name2:string,
      /**  Name Control, optional and used for electronic export  */  
   NameControl:string,
      /**  Payee Account Number  */  
   AccountNum:string,
      /**  Supplier TIN  */  
   TIN:string,
      /**  Ttime submitted electronically  */  
   TimeSubmitted:number,
      /**  Generation Date  */  
   GenDate:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Non US Supplier  */  
   NonUS:boolean,
      /**  FATCA  */  
   FATCA:boolean,
      /**  Form 1099-K Transaction Type  */  
   US1099KTranType:string,
      /**  Form 1099-K Merchant Category Code  */  
   US1099KMerchCatCode:string,
      /**  Plant  */  
   Plant:string,
      /**  Company Address  */  
   CompanyAddress:string,
      /**  Company Address 2nd Line  */  
   CompanyAddress2:string,
      /**  Company Address 3rd Line  */  
   CompanyAddress3:string,
      /**  City portion of company address  */  
   CompanyCity:string,
      /**  Company Name  */  
   CompanyName:string,
      /**  Company Name 2nd Line  */  
   CompanyName2:string,
      /**  State portion of company address  */  
   CompanyState:string,
      /**  Company TIN  */  
   CompanyTIN:string,
      /**  Postal code or zip code portion of company address.  */  
   CompanyZIP:string,
      /**  Company phone number  */  
   CountryPhone:string,
      /**  Check field to determine wheter the record was modified by the user or not.  */  
   ModifiedAndSaved:boolean,
   BitFlag:number,
   FormTypeDescription:string,
   VendorVendorNum:number,
   VendorNonUS:boolean,
   VendorAddress1:string,
   VendorCity:string,
   VendorAccountNum:string,
   VendorAddress2:string,
   VendorVendorID:string,
   VendorNameControl:string,
   VendorZIP:string,
   VendorReporting1099Name:string,
   VendorAddress3:string,
   VendorState:string,
   VendorCountryNum:number,
   VendorFATCA:boolean,
   VendorReporting1099Name2:string,
   VendorSecondTINNotice:boolean,
   VendorTINType:string,
   VendorTIN:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_Form1099Tableset{
   Form1099:Erp_Tablesets_Form1099Row[],
   Form1099Dtl:Erp_Tablesets_Form1099DtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtForm1099Tableset{
   Form1099:Erp_Tablesets_Form1099Row[],
   Form1099Dtl:Erp_Tablesets_Form1099DtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param formTypeID
      @param form1099Num
   */  
export interface GetByIDSite_input{
      /**  1099 Form Type  */  
   formTypeID:string,
      /**  1099 Form Number  */  
   form1099Num:number,
}

export interface GetByIDSite_output{
   returnObj:Erp_Tablesets_Form1099Tableset[],
parameters : {
      /**  output parameters  */  
   errorMessage:string,
}
}

   /** Required : 
      @param formTypeID
      @param form1099Num
   */  
export interface GetByID_input{
   formTypeID:string,
   form1099Num:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_Form1099Tableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_Form1099Tableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_Form1099Tableset[],
}

export interface GetDefaultFormType_output{
parameters : {
      /**  output parameters  */  
   defaultFormType:string,
   defaultFormTypeDesc:string,
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
   returnObj:Erp_Tablesets_Form1099ListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param formTypeID
      @param form1099Num
   */  
export interface GetNewForm1099Dtl_input{
   ds:Erp_Tablesets_Form1099Tableset[],
   formTypeID:string,
   form1099Num:number,
}

export interface GetNewForm1099Dtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_Form1099Tableset[],
}
}

   /** Required : 
      @param ds
      @param formTypeID
   */  
export interface GetNewForm1099_input{
   ds:Erp_Tablesets_Form1099Tableset[],
   formTypeID:string,
}

export interface GetNewForm1099_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_Form1099Tableset[],
}
}

   /** Required : 
      @param whereClauseForm1099
      @param whereClauseForm1099Dtl
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseForm1099:string,
   whereClauseForm1099Dtl:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_Form1099Tableset[],
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
      @param formTypeID
      @param p1099Code
      @param ds
   */  
export interface OnChange1099Code_input{
      /**  Form Type - Code for Form Type  */  
   formTypeID:string,
      /**  1099 Code - 1099 Code  */  
   p1099Code:string,
   ds:Erp_Tablesets_Form1099Tableset[],
}

export interface OnChange1099Code_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_Form1099Tableset[],
}
}

   /** Required : 
      @param formTypeID
      @param p1099Code
      @param boxAmount
   */  
export interface OnChangeBoxAmount_input{
      /**  Form Type - Code for Form Type  */  
   formTypeID:string,
      /**  1099 Code - 1099 Code  */  
   p1099Code:string,
      /**  Box Amount - Amount for the box line  */  
   boxAmount:number,
}

export interface OnChangeBoxAmount_output{
}

   /** Required : 
      @param formTypeID
      @param boxNum
      @param ds
   */  
export interface OnChangeBoxNum_input{
      /**  Form Type - Code for Form Type  */  
   formTypeID:string,
      /**  Box Number - Code for Box Number  */  
   boxNum:string,
   ds:Erp_Tablesets_Form1099Tableset[],
}

export interface OnChangeBoxNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_Form1099Tableset[],
}
}

   /** Required : 
      @param vendorId
      @param ds
   */  
export interface OnChangeVendor_input{
      /**  Vendor ID  */  
   vendorId:string,
   ds:Erp_Tablesets_Form1099Tableset[],
}

export interface OnChangeVendor_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_Form1099Tableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtForm1099Tableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtForm1099Tableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_Form1099Tableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_Form1099Tableset[],
}
}

   /** Required : 
      @param formTypeID
   */  
export interface ValidateFormTypeID_input{
   formTypeID:string,
}

export interface ValidateFormTypeID_output{
parameters : {
      /**  output parameters  */  
   formTypeIDDescription:string,
}
}

   /** Required : 
      @param formTypeID
      @param form1099Num
      @param ds
   */  
export interface ValidateUpdate_input{
      /**  Form Type - Code for Form Type  */  
   formTypeID:string,
      /**  Form Number - 1099 Form Number  */  
   form1099Num:number,
   ds:Erp_Tablesets_Form1099Tableset[],
}

export interface ValidateUpdate_output{
parameters : {
      /**  output parameters  */  
   pcresult:boolean,
   ds:Erp_Tablesets_Form1099Tableset[],
}
}

   /** Required : 
      @param formTypeID
      @param form1099Num
      @param ds
   */  
export interface Void1099Form_input{
      /**  Form Type - Code for Form Type  */  
   formTypeID:string,
      /**  Form Number - 1099 Form Number  */  
   form1099Num:number,
   ds:Erp_Tablesets_Form1099Tableset[],
}

export interface Void1099Form_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_Form1099Tableset[],
}
}

