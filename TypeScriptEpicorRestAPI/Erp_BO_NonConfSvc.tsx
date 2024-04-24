import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.NonConfSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/$metadata", {
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
   Description: Get NonConfs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_NonConfs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.NonConfRow
   */  
export function get_NonConfs(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_NonConfRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/NonConfs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_NonConfRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_NonConfs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.NonConfRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.NonConfRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_NonConfs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/NonConfs", {
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
   Summary: Calls GetByID to retrieve the NonConf item
   Description: Calls GetByID to retrieve the NonConf item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_NonConf
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TranID Desc: TranID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.NonConfRow
   */  
export function get_NonConfs_Company_TranID(Company:string, TranID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_NonConfRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/NonConfs(" + Company + "," + TranID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_NonConfRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update NonConf for the service
   Description: Calls UpdateExt to update NonConf. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_NonConf
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TranID Desc: TranID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.NonConfRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_NonConfs_Company_TranID(Company:string, TranID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/NonConfs(" + Company + "," + TranID + ")", {
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
   Summary: Call UpdateExt to delete NonConf item
   Description: Call UpdateExt to delete NonConf item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_NonConf
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TranID Desc: TranID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_NonConfs_Company_TranID(Company:string, TranID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/NonConfs(" + Company + "," + TranID + ")", {
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
   Description: Get NonConfAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_NonConfAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TranID Desc: TranID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.NonConfAttchRow
   */  
export function get_NonConfs_Company_TranID_NonConfAttches(Company:string, TranID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_NonConfAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/NonConfs(" + Company + "," + TranID + ")/NonConfAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_NonConfAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the NonConfAttch item
   Description: Calls GetByID to retrieve the NonConfAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_NonConfAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TranID Desc: TranID   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.NonConfAttchRow
   */  
export function get_NonConfs_Company_TranID_NonConfAttches_Company_TranID_DrawingSeq(Company:string, TranID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_NonConfAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/NonConfs(" + Company + "," + TranID + ")/NonConfAttches(" + Company + "," + TranID + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_NonConfAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get NonConfAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_NonConfAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.NonConfAttchRow
   */  
export function get_NonConfAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_NonConfAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/NonConfAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_NonConfAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_NonConfAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.NonConfAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.NonConfAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_NonConfAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/NonConfAttches", {
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
   Summary: Calls GetByID to retrieve the NonConfAttch item
   Description: Calls GetByID to retrieve the NonConfAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_NonConfAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TranID Desc: TranID   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.NonConfAttchRow
   */  
export function get_NonConfAttches_Company_TranID_DrawingSeq(Company:string, TranID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_NonConfAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/NonConfAttches(" + Company + "," + TranID + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_NonConfAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update NonConfAttch for the service
   Description: Calls UpdateExt to update NonConfAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_NonConfAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TranID Desc: TranID   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.NonConfAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_NonConfAttches_Company_TranID_DrawingSeq(Company:string, TranID:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/NonConfAttches(" + Company + "," + TranID + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete NonConfAttch item
   Description: Call UpdateExt to delete NonConfAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_NonConfAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TranID Desc: TranID   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_NonConfAttches_Company_TranID_DrawingSeq(Company:string, TranID:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/NonConfAttches(" + Company + "," + TranID + "," + DrawingSeq + ")", {
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
   Description: Get LegalNumGenOpts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LegalNumGenOpts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LegalNumGenOptsRow
   */  
export function get_LegalNumGenOpts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/LegalNumGenOpts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LegalNumGenOpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LegalNumGenOpts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/LegalNumGenOpts", {
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
   Summary: Calls GetByID to retrieve the LegalNumGenOpt item
   Description: Calls GetByID to retrieve the LegalNumGenOpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LegalNumGenOpt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LegalNumberID Desc: LegalNumberID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   */  
export function get_LegalNumGenOpts_Company_LegalNumberID(Company:string, LegalNumberID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LegalNumGenOptsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_LegalNumGenOptsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update LegalNumGenOpt for the service
   Description: Calls UpdateExt to update LegalNumGenOpt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LegalNumGenOpt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LegalNumberID Desc: LegalNumberID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_LegalNumGenOpts_Company_LegalNumberID(Company:string, LegalNumberID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
   Summary: Call UpdateExt to delete LegalNumGenOpt item
   Description: Call UpdateExt to delete LegalNumGenOpt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LegalNumGenOpt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LegalNumberID Desc: LegalNumberID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_LegalNumGenOpts_Company_LegalNumberID(Company:string, LegalNumberID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
   Description: Get SelectedSerialNumbers items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SelectedSerialNumbers
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SelectedSerialNumbersRow
   */  
export function get_SelectedSerialNumbers(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SelectedSerialNumbersRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/SelectedSerialNumbers", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SelectedSerialNumbersRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SelectedSerialNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SelectedSerialNumbers(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/SelectedSerialNumbers", {
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
   Summary: Calls GetByID to retrieve the SelectedSerialNumber item
   Description: Calls GetByID to retrieve the SelectedSerialNumber item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SelectedSerialNumber
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
   */  
export function get_SelectedSerialNumbers_Company_PartNum_SerialNumber(Company:string, PartNum:string, SerialNumber:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SelectedSerialNumbersRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_SelectedSerialNumbersRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update SelectedSerialNumber for the service
   Description: Calls UpdateExt to update SelectedSerialNumber. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SelectedSerialNumber
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_SelectedSerialNumbers_Company_PartNum_SerialNumber(Company:string, PartNum:string, SerialNumber:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", {
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
   Summary: Call UpdateExt to delete SelectedSerialNumber item
   Description: Call UpdateExt to delete SelectedSerialNumber item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SelectedSerialNumber
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_SelectedSerialNumbers_Company_PartNum_SerialNumber(Company:string, PartNum:string, SerialNumber:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", {
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
   Description: Get SNFormats items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SNFormats
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SNFormatRow
   */  
export function get_SNFormats(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SNFormatRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/SNFormats", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SNFormatRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SNFormats
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SNFormatRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SNFormatRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SNFormats(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/SNFormats", {
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
   Summary: Calls GetByID to retrieve the SNFormat item
   Description: Calls GetByID to retrieve the SNFormat item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SNFormat
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SNFormatRow
   */  
export function get_SNFormats_Company_PartNum_Plant(Company:string, PartNum:string, Plant:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SNFormatRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_SNFormatRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update SNFormat for the service
   Description: Calls UpdateExt to update SNFormat. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SNFormat
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SNFormatRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_SNFormats_Company_PartNum_Plant(Company:string, PartNum:string, Plant:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", {
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
   Summary: Call UpdateExt to delete SNFormat item
   Description: Call UpdateExt to delete SNFormat item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SNFormat
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_SNFormats_Company_PartNum_Plant(Company:string, PartNum:string, Plant:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.NonConfListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_NonConfListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_NonConfListRow)
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
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseNonConf:string, whereClauseNonConfAttch:string, whereClauseLegalNumGenOpts:string, whereClauseSelectedSerialNumbers:string, whereClauseSNFormat:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseNonConf!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseNonConf=" + whereClauseNonConf
   }
   if(typeof whereClauseNonConfAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseNonConfAttch=" + whereClauseNonConfAttch
   }
   if(typeof whereClauseLegalNumGenOpts!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLegalNumGenOpts=" + whereClauseLegalNumGenOpts
   }
   if(typeof whereClauseSelectedSerialNumbers!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSelectedSerialNumbers=" + whereClauseSelectedSerialNumbers
   }
   if(typeof whereClauseSNFormat!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSNFormat=" + whereClauseSNFormat
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/GetRows" + params, {
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(tranID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof tranID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "tranID=" + tranID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/GetList" + params, {
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
   Summary: Invoke method AddNewNonConfRow
   Description: Add NonConf of a certain type.  Valid types are Operation, Inventory, JobMaterial, SubContract, and Other.
Since Update() disallows changes to the TrnTyp field, you MUST use this instead of GetNewNonConf().
This method added to call from Kinetic UI
   OperationID: AddNewNonConfRow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddNewNonConfRow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddNewNonConfRow_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddNewNonConfRow(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/AddNewNonConfRow", {
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
   Summary: Invoke method AddNonConf
   Description: Add NonConf of a certain type.  Valid types are Operation, Inventory, JobMaterial, SubContract, and Other.
Since Update() disallows changes to the TrnTyp field, you MUST use this instead of GetNewNonConf().
   OperationID: AddNonConf
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddNonConf_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddNonConf_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddNonConf(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/AddNonConf", {
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
   Summary: Invoke method ChkPartXRefInfo
   Description: This method checks whether a cross-reference exists for the new part.
It should be executed when the Part number changed.
   OperationID: ChkPartXRefInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChkPartXRefInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChkPartXRefInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChkPartXRefInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/ChkPartXRefInfo", {
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
   Summary: Invoke method Get_PartRev
   Description: Get the latest Revision (as of TODAY) for the given Part.
   OperationID: Get_PartRev
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Get_PartRev_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Get_PartRev_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Get_PartRev(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/Get_PartRev", {
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
   Summary: Invoke method GetAvailableQty
   Description: Get the available quantity for the part/warehouse/bin/dim code/lot.
   OperationID: GetAvailableQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAvailableQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailableQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAvailableQty(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/GetAvailableQty", {
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
   Summary: Invoke method GetMtlQueueSeqValue
   Description: Search for the MtlQueueSeq value from the MtlQueue row related to the current Non Conformance.
   OperationID: GetMtlQueueSeqValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMtlQueueSeqValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMtlQueueSeqValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMtlQueueSeqValue(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/GetMtlQueueSeqValue", {
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
   Summary: Invoke method GetMtlSources
   Description: To retrieve the list of possible Material Sources for the given Job Material, as a dataset, to
facilitate presenting them to the user to pick one.  See the Pick Material Source dialog in
v6.10 (qae10-ml.w).
The purpose of determining the material source is to set NonConf.VendorNum and NonConf.PurPoint
in the case where the tranType = "PUR-MTL".
The user's selection of one of these should be stored in the NonConf.MtlSourceTrnType field
(i.e. NonConf.MtlSourceTrnType = NonConfSource.TrnType).
Note that in v6.10, the user is only presented with the dialog if the Job Material has
more than one possible source.  To support that behavior, this routine sets the output parameter
pcMtlSourceTrnType to the PartTran.TranType when it is unambiguous.
   OperationID: GetMtlSources
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMtlSources_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMtlSources_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMtlSources(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/GetMtlSources", {
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
   Summary: Invoke method GetPartInfo
   Description: For a given Part Number, retrieve the current Revision, Unit of Measure, Default Warehouse,
and whether it is tracked by Lot, and/or Dimension.
            
Any time the Part has changed, the Lot-, Dimension-, and SerialNumber-tracking attributes
need to be checked, and corresponding fields enabled/disabled as appropriate.  Also, the
SelectedSerialNumbers dataset needs to be cleared out.
   OperationID: GetPartInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPartInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/GetPartInfo", {
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
   Summary: Invoke method GetPartTranPKs
   Description: Returns primary keys of the part transaction related to the particular non conformance.
   OperationID: GetPartTranPKs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartTranPKs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartTranPKs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPartTranPKs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/GetPartTranPKs", {
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
   Summary: Invoke method GetSelectedSerialNumbers
   Description: This method will populate the SelectedSerialNumber datatable for the Non Conf RowIdent.
   OperationID: GetSelectedSerialNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSelectedSerialNumbers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectedSerialNumbers_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSelectedSerialNumbers(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/GetSelectedSerialNumbers", {
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
   Summary: Invoke method GetSelectedSerialNumbersParams
   Description: This method will populate the SelectedSerialNumber datatable for the Non Conf RowIdent.
   OperationID: GetSelectedSerialNumbersParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSelectedSerialNumbersParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectedSerialNumbersParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSelectedSerialNumbersParams(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/GetSelectedSerialNumbersParams", {
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
   Summary: Invoke method GetSelectSerialNumbersParams
   Description: Gets parameters required for launching Select Serial Numbers
   OperationID: GetSelectSerialNumbersParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSelectSerialNumbersParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectSerialNumbersParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSelectSerialNumbersParams(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/GetSelectSerialNumbersParams", {
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
   Summary: Invoke method OnChangeJobAsm
   Description: This method validates the ProposedAssemblySeq, then updates the following assembly-related fields:
NonConf.PartNum
NonConf.PartNumPartDescription
NonConf.RevisionNum
NonConf.ScrapUM
NonConf.WarehouseCode
NonConf.BinNum
NonConf.PartNumTrackSerialNum
NonConf.PartNumTrackLots
NonConf.PartNumTrackDimension
NonConf.OprSeq
NonConf.MtlSeq
NonConf.ResourceID
NonConf.ResourceIDDescription
            
This method should be run when the NonConf.AssemblySeq field changes.
            
Any time the Part has changed, the Lot-, Dimension-, and SerialNumber-tracking attributes
need to be checked, and corresponding fields enabled/disabled as appropriate.  Also, the
SelectedSerialNumbers dataset needs to be cleared out.
            
An exception is thrown if:
- No Job Assembly exists with the given Assembly Sequence Number
   OperationID: OnChangeJobAsm
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeJobAsm_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeJobAsm_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeJobAsm(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/OnChangeJobAsm", {
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
   Summary: Invoke method OnChangeJobMtl
   Description: This method validates the piProposedMtlSeq, then updates the following material-related fields:
NonConf.PartNum
NonConf.PartNumPartDescription
NonConf.RevisionNum
NonConf.ScrapUM
            
This method should be run when the NonConf.MtlSeq field changes.
            
Any time the Part has changed, the Lot-, Dimension-, and SerialNumber-tracking attributes
need to be checked, and corresponding fields enabled/disabled as appropriate.  Also, the
SelectedSerialNumbers dataset needs to be cleared out.
            
An exception is thrown if:
- No Job Material exists with the given MtlSeq Number
   OperationID: OnChangeJobMtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeJobMtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeJobMtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeJobMtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/OnChangeJobMtl", {
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
   Summary: Invoke method OnChangeJobNum
   Description: This method validates the JobNum, then updates the following Job-related fields:
PartNum, AssemblySeq, MtlSeq, OprSeq, ResourceID, ResourceIDDescription,
JobNumPartDescription, Plant
This method should be run when the NonConf.JobNum field changes.
            
If the Part related to the job has only one possible Assembly, the appropriate
assembly information is returned, and the plAsmReturned flag is returned as TRUE.  This
should be used to disable the Assembly Number field and lookup, if appropriate.
            
Any time the Part has changed, the Lot-, Dimension-, and SerialNumber-tracking attributes
need to be checked, and corresponding fields enabled/disabled as appropriate.  Also, the
SelectedSerialNumbers dataset needs to be cleared out.
            
An exception is thrown if:
- No Job exists with the given JobNum
- Job is not for current plant
- Job has been closed
- Job has not been released
- Job is for a service call that has been invoiced
   OperationID: OnChangeJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeJobNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/OnChangeJobNum", {
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
   Summary: Invoke method OnChangeBinNum
   Description: Method validates bins - both to and from
   OperationID: OnChangeBinNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeBinNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBinNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeBinNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/OnChangeBinNum", {
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
   Summary: Invoke method OnChangeWarehouseCode
   Description: Method validates warehouse codes - both to and from
   OperationID: OnChangeWarehouseCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeWarehouseCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeWarehouseCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeWarehouseCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/OnChangeWarehouseCode", {
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
   Summary: Invoke method OnChangeJobOpr
   Description: This method validates the piProposedOprSeq, then updates the following operation-related fields:
NonConf.OprSeq
NonConf.WCCode
NonConf.WrkCntrDesc
NonConf.WarehouseCode
NonConf.WarehouseCodeDescription
NonConf.BinNum
            
This method should be run when the NonConf.OprSeq field changes.
            
Any time the Part has changed, the Lot-, Dimension-, and SerialNumber-tracking attributes
need to be checked, and corresponding fields enabled/disabled as appropriate.  Also, the
SelectedSerialNumbers dataset needs to be cleared out.
            
An exception is thrown if:
- No Job Operation exists with the given OprSeq Number
   OperationID: OnChangeJobOpr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeJobOpr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeJobOpr_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeJobOpr(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/OnChangeJobOpr", {
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
   Summary: Invoke method OnChangeTranQty
   Description: Call this method when the value of Epicor.Mfg.BO.IssueReturnDataSet.TranQty changes.
This method performs validation on TranQty and sets the Issued Complete flag.
   OperationID: OnChangeTranQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeTranQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTranQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeTranQty(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/OnChangeTranQty", {
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
   Summary: Invoke method OnChangeUM
   Description: Call this method when the value of Epicor.Mfg.BO.IssueReturnDataSet.UM changes.
   OperationID: OnChangeUM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeUM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeUM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeUM(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/OnChangeUM", {
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
   Summary: Invoke method OnChangingRevisionNum
   Description: Call this method when the Revision changes to maintain inventory tracking
   OperationID: OnChangingRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingRevisionNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/OnChangingRevisionNum", {
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
   Summary: Invoke method OnChangeFromPCID
   Description: Validates that PCID exists
   OperationID: OnChangeFromPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeFromPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFromPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeFromPCID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/OnChangeFromPCID", {
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
   Summary: Invoke method OnChangeToPCID
   Description: Validates that PCID exists
   OperationID: OnChangeToPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeToPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeToPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeToPCID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/OnChangeToPCID", {
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
   Summary: Invoke method OnChangingAttributeSet
   Description: Call this method when the attribute set changes
   OperationID: OnChangingAttributeSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingAttributeSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingAttributeSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingAttributeSet(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/OnChangingAttributeSet", {
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
   Summary: Invoke method OnChangedCOPartNum
   Description: Call this method after coPartnum changes
   OperationID: OnChangedCOPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangedCOPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedCOPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangedCOPartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/OnChangedCOPartNum", {
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
   Summary: Invoke method PreUpdate
   Description: This method does:
1 - Returns a record in the LegalNumGenOpts datatable if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
   OperationID: PreUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreUpdate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/PreUpdate", {
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
   Summary: Invoke method ValidateSN
   Description: Validates that a single serial number is valid for this transaction
   OperationID: ValidateSN
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSN_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSN_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateSN(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/ValidateSN", {
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
   Summary: Invoke method GetReasonWhereClause
   Description: Provides a WHERE clause for obtaining a list of Reason codes suitable for the given type of
NonConformance.  Valid types are Operation, Inventory, JobMaterial, SubContract, and Other.
   OperationID: GetReasonWhereClause
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetReasonWhereClause_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReasonWhereClause_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetReasonWhereClause(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/GetReasonWhereClause", {
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
   Summary: Invoke method GetCodeDescList
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCodeDescList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/GetCodeDescList", {
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
   Summary: Invoke method GetAvailTranDocTypes
   OperationID: GetAvailTranDocTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailTranDocTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAvailTranDocTypes(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/GetAvailTranDocTypes", {
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
   Summary: Invoke method NegativeInventoryTest
   OperationID: NegativeInventoryTest
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/NegativeInventoryTest_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/NegativeInventoryTest_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_NegativeInventoryTest(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/NegativeInventoryTest", {
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
   Summary: Invoke method ValidateQtyInventoryTest
   OperationID: ValidateQtyInventoryTest
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateQtyInventoryTest_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateQtyInventoryTest_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateQtyInventoryTest(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/ValidateQtyInventoryTest", {
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
   Summary: Invoke method ValidateQtyInventoryTestIncludingPCID
   OperationID: ValidateQtyInventoryTestIncludingPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateQtyInventoryTestIncludingPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateQtyInventoryTestIncludingPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateQtyInventoryTestIncludingPCID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/ValidateQtyInventoryTestIncludingPCID", {
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
   Summary: Invoke method GetNewNonConf
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewNonConf
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewNonConf_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewNonConf_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewNonConf(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/GetNewNonConf", {
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
   Summary: Invoke method GetNewNonConfAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewNonConfAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewNonConfAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewNonConfAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewNonConfAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/GetNewNonConfAttch", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LegalNumGenOptsRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_NonConfAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_NonConfAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_NonConfListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_NonConfListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_NonConfRow{
   "odatametadata":string,
   "value":Erp_Tablesets_NonConfRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SNFormatRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SNFormatRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SelectedSerialNumbersRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SelectedSerialNumbersRow[],
}

export interface Erp_Tablesets_LegalNumGenOptsRow{
   "Company":string,
   "LegalNumberID":string,
   "TransYear":number,
   "TransYearSuffix":string,
   "DspTransYear":string,
      /**  Indicates if DspTransYear should be displayed when prompting for a manual number.  */  
   "ShowDspTransYear":boolean,
   "Prefix":string,
      /**  The list of prefixes that can be selected by the user for manual numbers.  */  
   "PrefixList":string,
      /**  The suffix portion of the legal number.  */  
   "NumberSuffix":string,
      /**  Indicates if the prefix can be entered by the user.  */  
   "EnablePrefix":boolean,
      /**  Indicates if the suffix (number) can be entered by the user.  */  
   "EnableSuffix":boolean,
   "NumberOption":string,
   "DocumentDate":string,
   "GenerationType":string,
   "Description":string,
   "TransPeriod":number,
      /**  Prefix for the period  */  
   "PeriodPrefix":string,
   "ShowTransPeriod":boolean,
      /**  Used when the full legal number is entered  */  
   "LegalNumber":string,
   "TranDocTypeID":string,
   "TranDocTypeID2":string,
   "GenerationOption":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_NonConfAttchRow{
   "Company":string,
   "TranID":number,
   "DrawingSeq":number,
   "XFileRefNum":number,
   "SysRevID":number,
   "SysRowID":string,
   "ForeignSysRowID":string,
   "DrawDesc":string,
   "FileName":string,
   "PDMDocID":string,
   "DocTypeID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_NonConfListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Quantity of the material to be scrapped.  */  
   "Quantity":number,
      /**  Scrap reason code.  */  
   "ReasonCode":string,
      /**  Job Number of the JobAsmbl record.  */  
   "JobNum":string,
      /**  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  */  
   "AssemblySeq":number,
      /**  A sequence number which uniquely identifies the material record within the Job/lot/level. The sequence can be system generated or assigned by user.  */  
   "MtlSeq":number,
      /**  The field that identifies the Part.  */  
   "PartNum":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
      /**  Scrap Labor Cost.  */  
   "ScrapLaborCost":number,
      /**  Scrap Burden Cost.  */  
   "ScrapBurdenCost":number,
      /**  Scrap Material Cost.  */  
   "ScrapMaterialCost":number,
      /**  Scrap Material Bur Cost.  */  
   "ScrapMaterialBurCost":number,
      /**   Internal code to identify the type of non-conformance.
Valid codes are:
"F" - First Article
"D" - Defective assemblies
"I" - Inventory
"M" - Job Materials
"S" - Subcontract
"P" - Purchase Order
"R" - RMA receipt
"O" - Other.  */  
   "TrnTyp":string,
      /**  Default dimension code for the part.  Set by selecting a PartDim record as default.  */  
   "DimCode":string,
      /**  The operation sequence of the Job/Assembly.  */  
   "OprSeq":number,
      /**  The ID of the Resource that was used to do the work. This field will be used to run reports using LaborDtl records to show how much work has been done on a specific Resource.  */  
   "ResourceID":string,
      /**  Describes the Part.  */  
   "Description":string,
      /**  This field is set equal to the Login ID variable.  System Set when a user creates the new transaction.  */  
   "EntryPerson":string,
      /**  Employee ID.  */  
   "EmpID":string,
      /**  To indicate if the record has been inspected (Open/Closed).  */  
   "InspectionPending":boolean,
      /**  Defines the Unit of Measure used when part is scrapped.  */  
   "ScrapUM":string,
      /**  The ID of the person that did the inspection.  Defaults to current DCD-UserID when the item has been inspected.  */  
   "InspectedBy":string,
      /**  The assigned Inspector ID that is going to perform the inspection. Assigned by the system using the current DCD-UserID when the item is being inspected.  Must be a valid Inspector ID, else it will be blank.  */  
   "InspectorID":string,
      /**  The conversion factor used to convert the material.  */  
   "DimConvFactor":number,
      /**  Used as the foreign key to the LaborDtl record.  */  
   "LaborHedSeq":number,
      /**  Used as a foreign key for LaborDtl record.  */  
   "LaborDtlSeq":number,
      /**  Total quantity that passed inspection to date.  In receiving unit of measure.  This is a summary maintained by the DMR process.  */  
   "PassedQty":number,
      /**  Total to date quantity that has failed inspection.  This is a summary maintained by the DMR process.  */  
   "FailedQty":number,
      /**  System date at time that record was created.  */  
   "SysDate":string,
      /**  System Time (hr-min-sec) when transaction was created.  */  
   "SysTime":number,
      /**  Contains comments about the transaction.  */  
   "PsdCommentText":string,
      /**  Contains comments about the transaction.  */  
   "FldCommentText":string,
      /**  Supplier Purchase Point  */  
   "PurPoint":string,
      /**  The internal key used to tie back to the Vendor master file.  */  
   "VendorNum":number,
      /**  Unique lot number for the part.  */  
   "LotNum":string,
      /**  Non conformance warehosue code  */  
   "WarehouseCode":string,
      /**  Identifies the Bin location that contains an Onhand quantity for this Part within a warehouse. The PartBin.BinNum can be blank (indicating bin tracking is not used for this part) or it  must be valid in the WhseBin table.  */  
   "BinNum":string,
      /**  Scrap Labor Cost.  */  
   "ScrapSubCost":number,
      /**  Indicate if the record was created from issued material or manufactured material. Valid values are "WIP", "INV" or blank.  */  
   "QtyFrm":string,
      /**  A unique number for the transaction.  Auto increment.  */  
   "TranID":number,
      /**  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  */  
   "DMRNum":number,
      /**  Purchase order that this release record is related to.  */  
   "PONum":number,
      /**  The line # of  PODetail record that the PORel record is related to.  */  
   "POLine":number,
      /**  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  */  
   "PORelNum":number,
      /**   Site Identifier. Always set as the Site that nonconf was created in.
Used as a filter to show only nonconf for the current Site.  */  
   "Plant":string,
      /**  Return Material Authorization Number of related RMAHead.  */  
   "RMANum":number,
      /**  Line number of the related RMADtl record.  */  
   "RMALine":number,
      /**  Receipt Number of related RMARcpt record.  */  
   "RMAReceipt":number,
      /**  Disposition Number of related RMADisp record.  */  
   "RMADisp":number,
      /**  Contains comments about the Non-Conformance transaction.  */  
   "CommentText":string,
      /**  Mtl Mtl unit cost to date.  */  
   "MaterialMtlCost":number,
      /**  Mtl Lab unit cost to date  */  
   "MaterialLabCost":number,
      /**  Mtl Sub Unit cost to date  */  
   "MaterialSubCost":number,
      /**  Material  Burd unit component cost to date  */  
   "MaterialBurCost":number,
      /**  Operation Master Code  */  
   "OpCode":string,
      /**  Warehouse where the quantity is moving to.  Defaults to "Inspection Warehouse" but can be overriden. Used in the Advanced material management.  */  
   "ToWarehouseCode":string,
      /**  Bin location that quantity will be moved to.  Used by Advanced Material Mgmt.  */  
   "ToBinNum":string,
      /**  This field holds the Non-conformance number that is generated by the Advanced Quality Module.  */  
   "AQMNCMNum":string,
      /**  Material Queue Records will only be updated if the "Request Move" box is checked  */  
   "RequestMove":boolean,
      /**   Move Cost to DMR option is used to define if some DMR transactions are accounted or not. In particular, for Non-Conformance Inspections, INS-DMR transactions related to Operation (NonConf.TrnTyp = 'D') are only booked when 'Moving Cost to DMR' is activated.
Default for 'Move Cost To DMR' flag is defined in Company level (Modules-Production-QA-Move Cost to DMR), however user can redefine it on Inspection processing UI for each Inspection.  */  
   "MoveCostsToDMR":boolean,
      /**  Transaction Document Type  */  
   "TranDocTypeID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  PCID  */  
   "PCID":string,
      /**  Full description of Reason... used on displays/reports.  */  
   "ReasonDescription":string,
      /**  For use with Material-type NonConfs: Holds the PartTran.TranType from the PartTran selected by the user, or "PUR-MTL"  */  
   "MtlSourceTrnType":string,
      /**  Descriptive code assigned by user which uniquely identifies a work center master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "ResourceGrpID":string,
      /**  Long description of the Work Center.  */  
   "WrkCntrDesc":string,
      /**  D='Operation' I="Inventory' M='Material' S='Subcontract' O='Other'  */  
   "TrnTypDescription":string,
   "LegalNumber":string,
   "LegalNumberMessage":string,
   "AllowNegQty":boolean,
   "AvailableQty":number,
      /**  To indicate if the record has been inspected (Open/Closed).  */  
   "Closed":boolean,
      /**  The ?Quantity? field converted to the UOM defined in the job material  */  
   "TranQty":number,
      /**  The UOM defined in the job material  */  
   "TranUOM":string,
      /**  The plant id of the plant that is controlling the serial tracking options, set depending on the IssueReturn UI  */  
   "SerialControlPlant":string,
      /**  If SerialControlPlantIsFromPlt = yes, then this field contains the to plant for the issue or return; it will be blank for Misc Issue  */  
   "SerialControlPlant2":string,
      /**  Indicates whether the plant in SerialControlPlant field is the from plant. Yes = is the from plant, No= is the to plant.  */  
   "SerialControlPlantIsFromPlt":boolean,
      /**  The process ID for the UI process that has created this IssueReturn record, only used by serial tracking logic  */  
   "ProcessID":string,
      /**  This external field would be used to indicate for the BL whether serial numbers should be validated/updated and indicated for the various UIs whether the serial number button will be enabled.  */  
   "EnableSN":boolean,
      /**  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  */  
   "AssemblySeqDescription":string,
      /**  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  */  
   "BinNumDescription":string,
      /**  Description for the dimension code.  */  
   "DimCodeDimCodeDescription":string,
      /**  Describes the Part.  System maintained, not user modifiable.  */  
   "DMRNumPartDescription":string,
      /**  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  */  
   "EmpIDName":string,
      /**  Inspector's Full Name.  */  
   "InspectorIDName":string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   "JobNumPartDescription":string,
      /**  Description of the operation.  Job, BOM, and Quote entry use this as a default description when entering operation details.  */  
   "OpCodeOpDesc":string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   "PartNumTrackLots":boolean,
      /**  Describes the Part.  */  
   "PartNumPartDescription":string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "PartNumSellingFactor":number,
      /**  Indicates if this part is serial number tracked  */  
   "PartNumTrackSerialNum":boolean,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   "PartNumPricePerCode":string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   "PartNumTrackDimension":boolean,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   "PartNumIUM":string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   "PartNumSalesUM":string,
      /**  The Plant name. Used on shipping reports.  */  
   "PlantName":string,
      /**  Supplier Part Number  */  
   "POLineVenPartNum":string,
      /**  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  */  
   "POLineLineDesc":string,
      /**  OUR internal Part number for this item.  */  
   "POLinePartNum":string,
      /**  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  */  
   "PORelNumRefCodeDesc":string,
      /**  Full description of Resource.  */  
   "ResourceIDDescription":string,
      /**  Line Item description. Defaults for OrderDtl if available, else from  Part master if available.  */  
   "RMALineLineDesc":string,
      /**  Description.  */  
   "ToWareHouseCodeDescDescription":string,
      /**  Second address line of the Supplier  */  
   "VendorNumAddress2":string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   "VendorNumTermsCode":string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   "VendorNumCountry":string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   "VendorNumName":string,
      /**  Third address line of the Supplier  */  
   "VendorNumAddress3":string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   "VendorNumVendorID":string,
      /**  A unique code that identifies the currency.  */  
   "VendorNumCurrencyCode":string,
      /**  First address line of the Supplier  */  
   "VendorNumAddress1":string,
      /**  Can be blank.  */  
   "VendorNumState":string,
      /**  City portion of the address of the Supplier  */  
   "VendorNumCity":string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   "VendorNumZIP":string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   "VendorNumDefaultFOB":string,
      /**  Description.  */  
   "WarehouseCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_NonConfRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Quantity of the material to be scrapped.  */  
   "Quantity":number,
      /**  Scrap reason code.  */  
   "ReasonCode":string,
      /**  Job Number of the JobAsmbl record.  */  
   "JobNum":string,
      /**  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  */  
   "AssemblySeq":number,
      /**  A sequence number which uniquely identifies the material record within the Job/lot/level. The sequence can be system generated or assigned by user.  */  
   "MtlSeq":number,
      /**  The field that identifies the Part.  */  
   "PartNum":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
      /**  Scrap Labor Cost.  */  
   "ScrapLaborCost":number,
      /**  Scrap Burden Cost.  */  
   "ScrapBurdenCost":number,
      /**  Scrap Material Cost.  */  
   "ScrapMaterialCost":number,
      /**  Scrap Material Bur Cost.  */  
   "ScrapMaterialBurCost":number,
      /**   Internal code to identify the type of non-conformance.
Valid codes are:
"F" - First Article
"D" - Defective assemblies
"I" - Inventory
"M" - Job Materials
"S" - Subcontract
"P" - Purchase Order
"R" - RMA receipt
"O" - Other.  */  
   "TrnTyp":string,
      /**  Default dimension code for the part.  Set by selecting a PartDim record as default.  */  
   "DimCode":string,
      /**  The operation sequence of the Job/Assembly.  */  
   "OprSeq":number,
      /**  The ID of the Resource that was used to do the work. This field will be used to run reports using LaborDtl records to show how much work has been done on a specific Resource.  */  
   "ResourceID":string,
      /**  Describes the Part.  */  
   "Description":string,
      /**  This field is set equal to the Login ID variable.  System Set when a user creates the new transaction.  */  
   "EntryPerson":string,
      /**  Employee ID.  */  
   "EmpID":string,
      /**  To indicate if the record has been inspected (Open/Closed).  */  
   "InspectionPending":boolean,
      /**  Defines the Unit of Measure used when part is scrapped.  */  
   "ScrapUM":string,
      /**  The ID of the person that did the inspection.  Defaults to current DCD-UserID when the item has been inspected.  */  
   "InspectedBy":string,
      /**  The assigned Inspector ID that is going to perform the inspection. Assigned by the system using the current DCD-UserID when the item is being inspected.  Must be a valid Inspector ID, else it will be blank.  */  
   "InspectorID":string,
      /**  The conversion factor used to convert the material.  */  
   "DimConvFactor":number,
      /**  Used as the foreign key to the LaborDtl record.  */  
   "LaborHedSeq":number,
      /**  Used as a foreign key for LaborDtl record.  */  
   "LaborDtlSeq":number,
      /**  Total quantity that passed inspection to date.  In receiving unit of measure.  This is a summary maintained by the DMR process.  */  
   "PassedQty":number,
      /**  Total to date quantity that has failed inspection.  This is a summary maintained by the DMR process.  */  
   "FailedQty":number,
      /**  System date at time that record was created.  */  
   "SysDate":string,
      /**  System Time (hr-min-sec) when transaction was created.  */  
   "SysTime":number,
      /**  Contains comments about the transaction.  */  
   "PsdCommentText":string,
      /**  Contains comments about the transaction.  */  
   "FldCommentText":string,
      /**  Supplier Purchase Point  */  
   "PurPoint":string,
      /**  The internal key used to tie back to the Vendor master file.  */  
   "VendorNum":number,
      /**  Unique lot number for the part.  */  
   "LotNum":string,
      /**  Non conformance warehosue code  */  
   "WarehouseCode":string,
      /**  Identifies the Bin location that contains an Onhand quantity for this Part within a warehouse. The PartBin.BinNum can be blank (indicating bin tracking is not used for this part) or it  must be valid in the WhseBin table.  */  
   "BinNum":string,
      /**  Scrap Labor Cost.  */  
   "ScrapSubCost":number,
      /**  Indicate if the record was created from issued material or manufactured material. Valid values are "WIP", "INV" or blank.  */  
   "QtyFrm":string,
      /**  A unique number for the transaction.  Auto increment.  */  
   "TranID":number,
      /**  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  */  
   "DMRNum":number,
      /**  Purchase order that this release record is related to.  */  
   "PONum":number,
      /**  The line # of  PODetail record that the PORel record is related to.  */  
   "POLine":number,
      /**  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  */  
   "PORelNum":number,
      /**   Site Identifier. Always set as the Site that nonconf was created in.
Used as a filter to show only nonconf for the current Site.  */  
   "Plant":string,
      /**  Return Material Authorization Number of related RMAHead.  */  
   "RMANum":number,
      /**  Line number of the related RMADtl record.  */  
   "RMALine":number,
      /**  Receipt Number of related RMARcpt record.  */  
   "RMAReceipt":number,
      /**  Disposition Number of related RMADisp record.  */  
   "RMADisp":number,
      /**  Contains comments about the Non-Conformance transaction.  */  
   "CommentText":string,
      /**  Mtl Mtl unit cost to date.  */  
   "MaterialMtlCost":number,
      /**  Mtl Lab unit cost to date  */  
   "MaterialLabCost":number,
      /**  Mtl Sub Unit cost to date  */  
   "MaterialSubCost":number,
      /**  Material  Burd unit component cost to date  */  
   "MaterialBurCost":number,
      /**  Operation Master Code  */  
   "OpCode":string,
      /**  Warehouse where the quantity is moving to.  Defaults to "Inspection Warehouse" but can be overriden. Used in the Advanced material management.  */  
   "ToWarehouseCode":string,
      /**  Bin location that quantity will be moved to.  Used by Advanced Material Mgmt.  */  
   "ToBinNum":string,
      /**  This field holds the Non-conformance number that is generated by the Advanced Quality Module.  */  
   "AQMNCMNum":string,
      /**  Material Queue Records will only be updated if the "Request Move" box is checked  */  
   "RequestMove":boolean,
      /**   Move Cost to DMR option is used to define if some DMR transactions are accounted or not. In particular, for Non-Conformance Inspections, INS-DMR transactions related to Operation (NonConf.TrnTyp = 'D') are only booked when 'Moving Cost to DMR' is activated.
Default for 'Move Cost To DMR' flag is defined in Company level (Modules-Production-QA-Move Cost to DMR), however user can redefine it on Inspection processing UI for each Inspection.  */  
   "MoveCostsToDMR":boolean,
      /**  Transaction Document Type  */  
   "TranDocTypeID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  PCID  */  
   "PCID":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Originating PCID.  */  
   "FromPCID":string,
   "AvailableQty":number,
      /**  To indicate if the record has been inspected (Open/Closed).  */  
   "Closed":boolean,
      /**  This external field would be used to indicate for the BL whether serial numbers should be validated/updated and indicated for the various UIs whether the serial number button will be enabled.  */  
   "EnableSN":boolean,
      /**  Operation code for reporting operation  */  
   "FromOpCode":string,
      /**  The operation reporting the nonconformance  */  
   "FromOprSeq":number,
   "LegalNumber":string,
   "LegalNumberMessage":string,
      /**  For use with Material-type NonConfs: Holds the PartTran.TranType from the PartTran selected by the user, or "PUR-MTL"  */  
   "MtlSourceTrnType":string,
      /**  The process ID for the UI process that has created this IssueReturn record, only used by serial tracking logic  */  
   "ProcessID":string,
      /**  Full description of Reason... used on displays/reports.  */  
   "ReasonDescription":string,
      /**  Descriptive code assigned by user which uniquely identifies a work center master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "ResourceGrpID":string,
      /**  The plant id of the plant that is controlling the serial tracking options, set depending on the IssueReturn UI  */  
   "SerialControlPlant":string,
      /**  If SerialControlPlantIsFromPlt = yes, then this field contains the to plant for the issue or return; it will be blank for Misc Issue  */  
   "SerialControlPlant2":string,
      /**  Indicates whether the plant in SerialControlPlant field is the from plant. Yes = is the from plant, No= is the to plant.  */  
   "SerialControlPlantIsFromPlt":boolean,
      /**  The ?Quantity? field converted to the UOM defined in the job material  */  
   "TranQty":number,
      /**  The UOM defined in the job material  */  
   "TranUOM":string,
      /**  D='Operation' I="Inventory' M='Material' S='Subcontract' O='Other'  */  
   "TrnTypDescription":string,
      /**  Long description of the Work Center.  */  
   "WrkCntrDesc":string,
   "AllowNegQty":boolean,
      /**  The Full Description of the Attribute Set.  */  
   "AttributeSetDescription":string,
      /**  The Short Description of the Attribute Set.  */  
   "AttributeSetShortDescription":string,
      /**  Search filter for AttributeSetID from multiple JobProd records  */  
   "JobProdAttrSearch":string,
      /**  multiple jobprod flag  */  
   "MultipleJobProd":boolean,
      /**  Operation Description  */  
   "FromOpCodeOpDesc":string,
      /**  True if TrnTyp = ‘I’ or TrnTyp = “D” (Operations) and co-parts exist for the job and AssemblySeq = 0 and it’s the final operation.  */  
   "EnablePartNum":boolean,
   "BitFlag":number,
   "AssemblySeqDescription":string,
   "BinNumDescription":string,
   "DimCodeDimCodeDescription":string,
   "DMRNumPartDescription":string,
   "EmpIDName":string,
   "InspectorIDName":string,
   "JobNumPartDescription":string,
   "OpCodeOpDesc":string,
   "PartNumAttrClassID":string,
   "PartNumTrackInventoryByRevision":boolean,
   "PartNumTrackInventoryAttributes":boolean,
   "PartNumSellingFactor":number,
   "PartNumTrackDimension":boolean,
   "PartNumIUM":string,
   "PartNumPricePerCode":string,
   "PartNumSalesUM":string,
   "PartNumTrackSerialNum":boolean,
   "PartNumTrackLots":boolean,
   "PartNumPartDescription":string,
   "PlantName":string,
   "POLinePartNum":string,
   "POLineLineDesc":string,
   "POLineVenPartNum":string,
   "ResourceIDDescription":string,
   "RMALineLineDesc":string,
   "ToBinNumDescription":string,
   "ToWareHouseCodeDescDescription":string,
   "VendorNumAddress2":string,
   "VendorNumName":string,
   "VendorNumTermsCode":string,
   "VendorNumDefaultFOB":string,
   "VendorNumState":string,
   "VendorNumVendorID":string,
   "VendorNumCurrencyCode":string,
   "VendorNumCity":string,
   "VendorNumCountry":string,
   "VendorNumAddress3":string,
   "VendorNumAddress1":string,
   "VendorNumZIP":string,
   "WarehouseCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_SNFormatRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Site Identifier. This field cannot be blank.  */  
   "Plant":string,
      /**  The PartNum field identifies the Part and is used in the primary key.  */  
   "PartNum":string,
      /**  Number of digits in the serial number  */  
   "NumberOfDigits":number,
      /**  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  */  
   "SNMask":string,
      /**   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  */  
   "SNBaseDataType":string,
   "SNFormat1":string,
      /**  Whether or not to have leading zeroes  */  
   "LeadingZeroes":boolean,
      /**   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  */  
   "SNPrefix":string,
      /**  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  */  
   "SNMaskSuffix":string,
      /**  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  */  
   "SNMaskPrefix":string,
      /**  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  */  
   "SNLastUsedSeq":string,
   "HasSerialNumbers":boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "PartPricePerCode":string,
   "PartTrackLots":boolean,
   "PartTrackSerialNum":boolean,
   "PartTrackDimension":boolean,
   "PartSalesUM":string,
   "PartIUM":string,
   "PartSellingFactor":number,
   "PartPartDescription":string,
   "SerialMaskMaskType":number,
   "SerialMaskMask":string,
   "SerialMaskExample":string,
   "SerialMaskDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_SelectedSerialNumbersRow{
      /**  Company  */  
   "Company":string,
      /**  SerialNumber  */  
   "SerialNumber":string,
      /**  Scrapped flag  */  
   "Scrapped":boolean,
      /**  Scrapped reason code  */  
   "ScrappedReasonCode":string,
      /**  Voided flag  */  
   "Voided":boolean,
      /**  Reference field  */  
   "Reference":string,
      /**  Reason code type = s  */  
   "ReasonCodeType":string,
      /**  Reason code description  */  
   "ReasonCodeDesc":string,
      /**  PartNumber  */  
   "PartNum":string,
      /**  Serial number prefix  */  
   "SNPrefix":string,
      /**  Base number used to create the serial number  */  
   "SNBaseNumber":string,
      /**  RowID of the source record for this serial number  */  
   "SourceRowID":string,
      /**  TransType of the record that created this serial number  */  
   "TransType":string,
      /**  True if this serial numbered part passed inspection  */  
   "PassedInspection":boolean,
      /**  Used to flag previously selected serial numbers as deselected  */  
   "Deselected":boolean,
   "KitWhseList":string,
      /**  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a validate type mask was being used where characters were stripped (using ~ in the mask).  */  
   "RawSerialNum":string,
      /**  Action type field used for Kanban receipts to indicate if the new serial number status is Inventory, Scrapped or NonConf.  This requires Code/desc:  1 ` inventory 2 ` Scrapped 3 ` Nonconformance  */  
   "KBLbrAction":number,
      /**  Description field for KBLbrAction ? holds the translated description for the KBLbrAction code for UI display and combo box.  */  
   "KBLbrActionDesc":string,
      /**  If true, then users can not deselect this serial number.  This is used by applications that allow maintenance to the Selected Serial Numbers after update.  */  
   "PreventDeselect":boolean,
      /**  Used only by SN Assignment  */  
   "XRefPartNum":string,
      /**  Used only by SN Assignment: C = Customer Part / I = Internal Part XRef  */  
   "XRefPartType":string,
   "PreDeselected":boolean,
      /**  temporary field used to link the packout lines to ship detail lines  */  
   "poLinkValues":string,
      /**  The mask the was used to generate the serial number  */  
   "SNMask":string,
      /**  Flag to indicate that the SelectedSerialNumbers entry has not yet been saved to the DB for the related transaction. Used to keep track of which deselected serial numbers need to be passed to the transaction update logic.  */  
   "NotSavedToDB":boolean,
   "RowSelected":boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param pcNonConfType
      @param ds
   */  
export interface AddNewNonConfRow_input{
      /**  Type/origin of NonConformance.  */  
   pcNonConfType:string,
   ds:Erp_Tablesets_NonConfTableset[],
}

export interface AddNewNonConfRow_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NonConfTableset[],
}
}

   /** Required : 
      @param pcNonConfType
   */  
export interface AddNonConf_input{
      /**  Type/origin of NonConformance.  */  
   pcNonConfType:string,
}

export interface AddNonConf_output{
   returnObj:Erp_Tablesets_NonConfTableset[],
}

   /** Required : 
      @param newPartNum
      @param SysRowID
      @param rowType
      @param uomCode
      @param ds
   */  
export interface ChkPartXRefInfo_input{
      /**  New Part Number  */  
   newPartNum:string,
      /**  RowID of the selected record. Skips find part logic if this has a value.  */  
   SysRowID:string,
      /**  RowType of the selected record. Only used with sysRowID.  */  
   rowType:string,
      /**  UOM Code (only used for Product Codes)  */  
   uomCode:string,
   ds:Erp_Tablesets_NonConfTableset[],
}

export interface ChkPartXRefInfo_output{
parameters : {
      /**  output parameters  */  
   newPartNum:string,
   uomCode:string,
   multipleMatch:boolean,
   ds:Erp_Tablesets_NonConfTableset[],
}
}

   /** Required : 
      @param tranID
   */  
export interface DeleteByID_input{
   tranID:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_LegalNumGenOptsRow{
   Company:string,
   LegalNumberID:string,
   TransYear:number,
   TransYearSuffix:string,
   DspTransYear:string,
      /**  Indicates if DspTransYear should be displayed when prompting for a manual number.  */  
   ShowDspTransYear:boolean,
   Prefix:string,
      /**  The list of prefixes that can be selected by the user for manual numbers.  */  
   PrefixList:string,
      /**  The suffix portion of the legal number.  */  
   NumberSuffix:string,
      /**  Indicates if the prefix can be entered by the user.  */  
   EnablePrefix:boolean,
      /**  Indicates if the suffix (number) can be entered by the user.  */  
   EnableSuffix:boolean,
   NumberOption:string,
   DocumentDate:string,
   GenerationType:string,
   Description:string,
   TransPeriod:number,
      /**  Prefix for the period  */  
   PeriodPrefix:string,
   ShowTransPeriod:boolean,
      /**  Used when the full legal number is entered  */  
   LegalNumber:string,
   TranDocTypeID:string,
   TranDocTypeID2:string,
   GenerationOption:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_NonConfAttchRow{
   Company:string,
   TranID:number,
   DrawingSeq:number,
   XFileRefNum:number,
   SysRevID:number,
   SysRowID:string,
   ForeignSysRowID:string,
   DrawDesc:string,
   FileName:string,
   PDMDocID:string,
   DocTypeID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_NonConfListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Quantity of the material to be scrapped.  */  
   Quantity:number,
      /**  Scrap reason code.  */  
   ReasonCode:string,
      /**  Job Number of the JobAsmbl record.  */  
   JobNum:string,
      /**  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  */  
   AssemblySeq:number,
      /**  A sequence number which uniquely identifies the material record within the Job/lot/level. The sequence can be system generated or assigned by user.  */  
   MtlSeq:number,
      /**  The field that identifies the Part.  */  
   PartNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  Scrap Labor Cost.  */  
   ScrapLaborCost:number,
      /**  Scrap Burden Cost.  */  
   ScrapBurdenCost:number,
      /**  Scrap Material Cost.  */  
   ScrapMaterialCost:number,
      /**  Scrap Material Bur Cost.  */  
   ScrapMaterialBurCost:number,
      /**   Internal code to identify the type of non-conformance.
Valid codes are:
"F" - First Article
"D" - Defective assemblies
"I" - Inventory
"M" - Job Materials
"S" - Subcontract
"P" - Purchase Order
"R" - RMA receipt
"O" - Other.  */  
   TrnTyp:string,
      /**  Default dimension code for the part.  Set by selecting a PartDim record as default.  */  
   DimCode:string,
      /**  The operation sequence of the Job/Assembly.  */  
   OprSeq:number,
      /**  The ID of the Resource that was used to do the work. This field will be used to run reports using LaborDtl records to show how much work has been done on a specific Resource.  */  
   ResourceID:string,
      /**  Describes the Part.  */  
   Description:string,
      /**  This field is set equal to the Login ID variable.  System Set when a user creates the new transaction.  */  
   EntryPerson:string,
      /**  Employee ID.  */  
   EmpID:string,
      /**  To indicate if the record has been inspected (Open/Closed).  */  
   InspectionPending:boolean,
      /**  Defines the Unit of Measure used when part is scrapped.  */  
   ScrapUM:string,
      /**  The ID of the person that did the inspection.  Defaults to current DCD-UserID when the item has been inspected.  */  
   InspectedBy:string,
      /**  The assigned Inspector ID that is going to perform the inspection. Assigned by the system using the current DCD-UserID when the item is being inspected.  Must be a valid Inspector ID, else it will be blank.  */  
   InspectorID:string,
      /**  The conversion factor used to convert the material.  */  
   DimConvFactor:number,
      /**  Used as the foreign key to the LaborDtl record.  */  
   LaborHedSeq:number,
      /**  Used as a foreign key for LaborDtl record.  */  
   LaborDtlSeq:number,
      /**  Total quantity that passed inspection to date.  In receiving unit of measure.  This is a summary maintained by the DMR process.  */  
   PassedQty:number,
      /**  Total to date quantity that has failed inspection.  This is a summary maintained by the DMR process.  */  
   FailedQty:number,
      /**  System date at time that record was created.  */  
   SysDate:string,
      /**  System Time (hr-min-sec) when transaction was created.  */  
   SysTime:number,
      /**  Contains comments about the transaction.  */  
   PsdCommentText:string,
      /**  Contains comments about the transaction.  */  
   FldCommentText:string,
      /**  Supplier Purchase Point  */  
   PurPoint:string,
      /**  The internal key used to tie back to the Vendor master file.  */  
   VendorNum:number,
      /**  Unique lot number for the part.  */  
   LotNum:string,
      /**  Non conformance warehosue code  */  
   WarehouseCode:string,
      /**  Identifies the Bin location that contains an Onhand quantity for this Part within a warehouse. The PartBin.BinNum can be blank (indicating bin tracking is not used for this part) or it  must be valid in the WhseBin table.  */  
   BinNum:string,
      /**  Scrap Labor Cost.  */  
   ScrapSubCost:number,
      /**  Indicate if the record was created from issued material or manufactured material. Valid values are "WIP", "INV" or blank.  */  
   QtyFrm:string,
      /**  A unique number for the transaction.  Auto increment.  */  
   TranID:number,
      /**  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  */  
   DMRNum:number,
      /**  Purchase order that this release record is related to.  */  
   PONum:number,
      /**  The line # of  PODetail record that the PORel record is related to.  */  
   POLine:number,
      /**  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  */  
   PORelNum:number,
      /**   Site Identifier. Always set as the Site that nonconf was created in.
Used as a filter to show only nonconf for the current Site.  */  
   Plant:string,
      /**  Return Material Authorization Number of related RMAHead.  */  
   RMANum:number,
      /**  Line number of the related RMADtl record.  */  
   RMALine:number,
      /**  Receipt Number of related RMARcpt record.  */  
   RMAReceipt:number,
      /**  Disposition Number of related RMADisp record.  */  
   RMADisp:number,
      /**  Contains comments about the Non-Conformance transaction.  */  
   CommentText:string,
      /**  Mtl Mtl unit cost to date.  */  
   MaterialMtlCost:number,
      /**  Mtl Lab unit cost to date  */  
   MaterialLabCost:number,
      /**  Mtl Sub Unit cost to date  */  
   MaterialSubCost:number,
      /**  Material  Burd unit component cost to date  */  
   MaterialBurCost:number,
      /**  Operation Master Code  */  
   OpCode:string,
      /**  Warehouse where the quantity is moving to.  Defaults to "Inspection Warehouse" but can be overriden. Used in the Advanced material management.  */  
   ToWarehouseCode:string,
      /**  Bin location that quantity will be moved to.  Used by Advanced Material Mgmt.  */  
   ToBinNum:string,
      /**  This field holds the Non-conformance number that is generated by the Advanced Quality Module.  */  
   AQMNCMNum:string,
      /**  Material Queue Records will only be updated if the "Request Move" box is checked  */  
   RequestMove:boolean,
      /**   Move Cost to DMR option is used to define if some DMR transactions are accounted or not. In particular, for Non-Conformance Inspections, INS-DMR transactions related to Operation (NonConf.TrnTyp = 'D') are only booked when 'Moving Cost to DMR' is activated.
Default for 'Move Cost To DMR' flag is defined in Company level (Modules-Production-QA-Move Cost to DMR), however user can redefine it on Inspection processing UI for each Inspection.  */  
   MoveCostsToDMR:boolean,
      /**  Transaction Document Type  */  
   TranDocTypeID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  PCID  */  
   PCID:string,
      /**  Full description of Reason... used on displays/reports.  */  
   ReasonDescription:string,
      /**  For use with Material-type NonConfs: Holds the PartTran.TranType from the PartTran selected by the user, or "PUR-MTL"  */  
   MtlSourceTrnType:string,
      /**  Descriptive code assigned by user which uniquely identifies a work center master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   ResourceGrpID:string,
      /**  Long description of the Work Center.  */  
   WrkCntrDesc:string,
      /**  D='Operation' I="Inventory' M='Material' S='Subcontract' O='Other'  */  
   TrnTypDescription:string,
   LegalNumber:string,
   LegalNumberMessage:string,
   AllowNegQty:boolean,
   AvailableQty:number,
      /**  To indicate if the record has been inspected (Open/Closed).  */  
   Closed:boolean,
      /**  The ?Quantity? field converted to the UOM defined in the job material  */  
   TranQty:number,
      /**  The UOM defined in the job material  */  
   TranUOM:string,
      /**  The plant id of the plant that is controlling the serial tracking options, set depending on the IssueReturn UI  */  
   SerialControlPlant:string,
      /**  If SerialControlPlantIsFromPlt = yes, then this field contains the to plant for the issue or return; it will be blank for Misc Issue  */  
   SerialControlPlant2:string,
      /**  Indicates whether the plant in SerialControlPlant field is the from plant. Yes = is the from plant, No= is the to plant.  */  
   SerialControlPlantIsFromPlt:boolean,
      /**  The process ID for the UI process that has created this IssueReturn record, only used by serial tracking logic  */  
   ProcessID:string,
      /**  This external field would be used to indicate for the BL whether serial numbers should be validated/updated and indicated for the various UIs whether the serial number button will be enabled.  */  
   EnableSN:boolean,
      /**  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  */  
   AssemblySeqDescription:string,
      /**  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  */  
   BinNumDescription:string,
      /**  Description for the dimension code.  */  
   DimCodeDimCodeDescription:string,
      /**  Describes the Part.  System maintained, not user modifiable.  */  
   DMRNumPartDescription:string,
      /**  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  */  
   EmpIDName:string,
      /**  Inspector's Full Name.  */  
   InspectorIDName:string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   JobNumPartDescription:string,
      /**  Description of the operation.  Job, BOM, and Quote entry use this as a default description when entering operation details.  */  
   OpCodeOpDesc:string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   PartNumTrackLots:boolean,
      /**  Describes the Part.  */  
   PartNumPartDescription:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   PartNumSellingFactor:number,
      /**  Indicates if this part is serial number tracked  */  
   PartNumTrackSerialNum:boolean,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   PartNumPricePerCode:string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   PartNumTrackDimension:boolean,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   PartNumIUM:string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   PartNumSalesUM:string,
      /**  The Plant name. Used on shipping reports.  */  
   PlantName:string,
      /**  Supplier Part Number  */  
   POLineVenPartNum:string,
      /**  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  */  
   POLineLineDesc:string,
      /**  OUR internal Part number for this item.  */  
   POLinePartNum:string,
      /**  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  */  
   PORelNumRefCodeDesc:string,
      /**  Full description of Resource.  */  
   ResourceIDDescription:string,
      /**  Line Item description. Defaults for OrderDtl if available, else from  Part master if available.  */  
   RMALineLineDesc:string,
      /**  Description.  */  
   ToWareHouseCodeDescDescription:string,
      /**  Second address line of the Supplier  */  
   VendorNumAddress2:string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   VendorNumTermsCode:string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   VendorNumCountry:string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   VendorNumName:string,
      /**  Third address line of the Supplier  */  
   VendorNumAddress3:string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   VendorNumVendorID:string,
      /**  A unique code that identifies the currency.  */  
   VendorNumCurrencyCode:string,
      /**  First address line of the Supplier  */  
   VendorNumAddress1:string,
      /**  Can be blank.  */  
   VendorNumState:string,
      /**  City portion of the address of the Supplier  */  
   VendorNumCity:string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   VendorNumZIP:string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   VendorNumDefaultFOB:string,
      /**  Description.  */  
   WarehouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_NonConfListTableset{
   NonConfList:Erp_Tablesets_NonConfListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_NonConfRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Quantity of the material to be scrapped.  */  
   Quantity:number,
      /**  Scrap reason code.  */  
   ReasonCode:string,
      /**  Job Number of the JobAsmbl record.  */  
   JobNum:string,
      /**  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  */  
   AssemblySeq:number,
      /**  A sequence number which uniquely identifies the material record within the Job/lot/level. The sequence can be system generated or assigned by user.  */  
   MtlSeq:number,
      /**  The field that identifies the Part.  */  
   PartNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  Scrap Labor Cost.  */  
   ScrapLaborCost:number,
      /**  Scrap Burden Cost.  */  
   ScrapBurdenCost:number,
      /**  Scrap Material Cost.  */  
   ScrapMaterialCost:number,
      /**  Scrap Material Bur Cost.  */  
   ScrapMaterialBurCost:number,
      /**   Internal code to identify the type of non-conformance.
Valid codes are:
"F" - First Article
"D" - Defective assemblies
"I" - Inventory
"M" - Job Materials
"S" - Subcontract
"P" - Purchase Order
"R" - RMA receipt
"O" - Other.  */  
   TrnTyp:string,
      /**  Default dimension code for the part.  Set by selecting a PartDim record as default.  */  
   DimCode:string,
      /**  The operation sequence of the Job/Assembly.  */  
   OprSeq:number,
      /**  The ID of the Resource that was used to do the work. This field will be used to run reports using LaborDtl records to show how much work has been done on a specific Resource.  */  
   ResourceID:string,
      /**  Describes the Part.  */  
   Description:string,
      /**  This field is set equal to the Login ID variable.  System Set when a user creates the new transaction.  */  
   EntryPerson:string,
      /**  Employee ID.  */  
   EmpID:string,
      /**  To indicate if the record has been inspected (Open/Closed).  */  
   InspectionPending:boolean,
      /**  Defines the Unit of Measure used when part is scrapped.  */  
   ScrapUM:string,
      /**  The ID of the person that did the inspection.  Defaults to current DCD-UserID when the item has been inspected.  */  
   InspectedBy:string,
      /**  The assigned Inspector ID that is going to perform the inspection. Assigned by the system using the current DCD-UserID when the item is being inspected.  Must be a valid Inspector ID, else it will be blank.  */  
   InspectorID:string,
      /**  The conversion factor used to convert the material.  */  
   DimConvFactor:number,
      /**  Used as the foreign key to the LaborDtl record.  */  
   LaborHedSeq:number,
      /**  Used as a foreign key for LaborDtl record.  */  
   LaborDtlSeq:number,
      /**  Total quantity that passed inspection to date.  In receiving unit of measure.  This is a summary maintained by the DMR process.  */  
   PassedQty:number,
      /**  Total to date quantity that has failed inspection.  This is a summary maintained by the DMR process.  */  
   FailedQty:number,
      /**  System date at time that record was created.  */  
   SysDate:string,
      /**  System Time (hr-min-sec) when transaction was created.  */  
   SysTime:number,
      /**  Contains comments about the transaction.  */  
   PsdCommentText:string,
      /**  Contains comments about the transaction.  */  
   FldCommentText:string,
      /**  Supplier Purchase Point  */  
   PurPoint:string,
      /**  The internal key used to tie back to the Vendor master file.  */  
   VendorNum:number,
      /**  Unique lot number for the part.  */  
   LotNum:string,
      /**  Non conformance warehosue code  */  
   WarehouseCode:string,
      /**  Identifies the Bin location that contains an Onhand quantity for this Part within a warehouse. The PartBin.BinNum can be blank (indicating bin tracking is not used for this part) or it  must be valid in the WhseBin table.  */  
   BinNum:string,
      /**  Scrap Labor Cost.  */  
   ScrapSubCost:number,
      /**  Indicate if the record was created from issued material or manufactured material. Valid values are "WIP", "INV" or blank.  */  
   QtyFrm:string,
      /**  A unique number for the transaction.  Auto increment.  */  
   TranID:number,
      /**  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  */  
   DMRNum:number,
      /**  Purchase order that this release record is related to.  */  
   PONum:number,
      /**  The line # of  PODetail record that the PORel record is related to.  */  
   POLine:number,
      /**  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  */  
   PORelNum:number,
      /**   Site Identifier. Always set as the Site that nonconf was created in.
Used as a filter to show only nonconf for the current Site.  */  
   Plant:string,
      /**  Return Material Authorization Number of related RMAHead.  */  
   RMANum:number,
      /**  Line number of the related RMADtl record.  */  
   RMALine:number,
      /**  Receipt Number of related RMARcpt record.  */  
   RMAReceipt:number,
      /**  Disposition Number of related RMADisp record.  */  
   RMADisp:number,
      /**  Contains comments about the Non-Conformance transaction.  */  
   CommentText:string,
      /**  Mtl Mtl unit cost to date.  */  
   MaterialMtlCost:number,
      /**  Mtl Lab unit cost to date  */  
   MaterialLabCost:number,
      /**  Mtl Sub Unit cost to date  */  
   MaterialSubCost:number,
      /**  Material  Burd unit component cost to date  */  
   MaterialBurCost:number,
      /**  Operation Master Code  */  
   OpCode:string,
      /**  Warehouse where the quantity is moving to.  Defaults to "Inspection Warehouse" but can be overriden. Used in the Advanced material management.  */  
   ToWarehouseCode:string,
      /**  Bin location that quantity will be moved to.  Used by Advanced Material Mgmt.  */  
   ToBinNum:string,
      /**  This field holds the Non-conformance number that is generated by the Advanced Quality Module.  */  
   AQMNCMNum:string,
      /**  Material Queue Records will only be updated if the "Request Move" box is checked  */  
   RequestMove:boolean,
      /**   Move Cost to DMR option is used to define if some DMR transactions are accounted or not. In particular, for Non-Conformance Inspections, INS-DMR transactions related to Operation (NonConf.TrnTyp = 'D') are only booked when 'Moving Cost to DMR' is activated.
Default for 'Move Cost To DMR' flag is defined in Company level (Modules-Production-QA-Move Cost to DMR), however user can redefine it on Inspection processing UI for each Inspection.  */  
   MoveCostsToDMR:boolean,
      /**  Transaction Document Type  */  
   TranDocTypeID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  PCID  */  
   PCID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Originating PCID.  */  
   FromPCID:string,
   AvailableQty:number,
      /**  To indicate if the record has been inspected (Open/Closed).  */  
   Closed:boolean,
      /**  This external field would be used to indicate for the BL whether serial numbers should be validated/updated and indicated for the various UIs whether the serial number button will be enabled.  */  
   EnableSN:boolean,
      /**  Operation code for reporting operation  */  
   FromOpCode:string,
      /**  The operation reporting the nonconformance  */  
   FromOprSeq:number,
   LegalNumber:string,
   LegalNumberMessage:string,
      /**  For use with Material-type NonConfs: Holds the PartTran.TranType from the PartTran selected by the user, or "PUR-MTL"  */  
   MtlSourceTrnType:string,
      /**  The process ID for the UI process that has created this IssueReturn record, only used by serial tracking logic  */  
   ProcessID:string,
      /**  Full description of Reason... used on displays/reports.  */  
   ReasonDescription:string,
      /**  Descriptive code assigned by user which uniquely identifies a work center master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   ResourceGrpID:string,
      /**  The plant id of the plant that is controlling the serial tracking options, set depending on the IssueReturn UI  */  
   SerialControlPlant:string,
      /**  If SerialControlPlantIsFromPlt = yes, then this field contains the to plant for the issue or return; it will be blank for Misc Issue  */  
   SerialControlPlant2:string,
      /**  Indicates whether the plant in SerialControlPlant field is the from plant. Yes = is the from plant, No= is the to plant.  */  
   SerialControlPlantIsFromPlt:boolean,
      /**  The ?Quantity? field converted to the UOM defined in the job material  */  
   TranQty:number,
      /**  The UOM defined in the job material  */  
   TranUOM:string,
      /**  D='Operation' I="Inventory' M='Material' S='Subcontract' O='Other'  */  
   TrnTypDescription:string,
      /**  Long description of the Work Center.  */  
   WrkCntrDesc:string,
   AllowNegQty:boolean,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
      /**  Search filter for AttributeSetID from multiple JobProd records  */  
   JobProdAttrSearch:string,
      /**  multiple jobprod flag  */  
   MultipleJobProd:boolean,
      /**  Operation Description  */  
   FromOpCodeOpDesc:string,
      /**  True if TrnTyp = ‘I’ or TrnTyp = “D” (Operations) and co-parts exist for the job and AssemblySeq = 0 and it’s the final operation.  */  
   EnablePartNum:boolean,
   BitFlag:number,
   AssemblySeqDescription:string,
   BinNumDescription:string,
   DimCodeDimCodeDescription:string,
   DMRNumPartDescription:string,
   EmpIDName:string,
   InspectorIDName:string,
   JobNumPartDescription:string,
   OpCodeOpDesc:string,
   PartNumAttrClassID:string,
   PartNumTrackInventoryByRevision:boolean,
   PartNumTrackInventoryAttributes:boolean,
   PartNumSellingFactor:number,
   PartNumTrackDimension:boolean,
   PartNumIUM:string,
   PartNumPricePerCode:string,
   PartNumSalesUM:string,
   PartNumTrackSerialNum:boolean,
   PartNumTrackLots:boolean,
   PartNumPartDescription:string,
   PlantName:string,
   POLinePartNum:string,
   POLineLineDesc:string,
   POLineVenPartNum:string,
   ResourceIDDescription:string,
   RMALineLineDesc:string,
   ToBinNumDescription:string,
   ToWareHouseCodeDescDescription:string,
   VendorNumAddress2:string,
   VendorNumName:string,
   VendorNumTermsCode:string,
   VendorNumDefaultFOB:string,
   VendorNumState:string,
   VendorNumVendorID:string,
   VendorNumCurrencyCode:string,
   VendorNumCity:string,
   VendorNumCountry:string,
   VendorNumAddress3:string,
   VendorNumAddress1:string,
   VendorNumZIP:string,
   WarehouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_NonConfSourceRow{
      /**  Job Number that transaction is associated with.  */  
   JobNum:string,
      /**  Assembly Sequence #  */  
   AssemblySeq:number,
      /**  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  */  
   MtlSeq:number,
      /**  Field that indicates the type of transaction: copied from PartTran.TranType  */  
   TrnType:string,
      /**  Transaction Quantity  */  
   TrnQty:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_NonConfSourceTableset{
   NonConfSource:Erp_Tablesets_NonConfSourceRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_NonConfTableset{
   NonConf:Erp_Tablesets_NonConfRow[],
   NonConfAttch:Erp_Tablesets_NonConfAttchRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   SelectedSerialNumbers:Erp_Tablesets_SelectedSerialNumbersRow[],
   SNFormat:Erp_Tablesets_SNFormatRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_SNFormatRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Site Identifier. This field cannot be blank.  */  
   Plant:string,
      /**  The PartNum field identifies the Part and is used in the primary key.  */  
   PartNum:string,
      /**  Number of digits in the serial number  */  
   NumberOfDigits:number,
      /**  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  */  
   SNMask:string,
      /**   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  */  
   SNBaseDataType:string,
      /**   Current setting for Format of the Base serial number that will be used as new serial numbers are generated. Expressed in progress syntax. Ex: X(30), 99999999 for Character or Integer, or as a Serial Mask defined in SerialMask table.
This field should be flagged as ReadOnly and Include = true in Object Designer.  */  
   SNFormat:string,
      /**  Whether or not to have leading zeroes  */  
   LeadingZeroes:boolean,
      /**   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  */  
   SNPrefix:string,
      /**  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  */  
   SNMaskSuffix:string,
      /**  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  */  
   SNMaskPrefix:string,
      /**  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  */  
   SNLastUsedSeq:string,
   HasSerialNumbers:boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   PartPricePerCode:string,
   PartTrackLots:boolean,
   PartTrackSerialNum:boolean,
   PartTrackDimension:boolean,
   PartSalesUM:string,
   PartIUM:string,
   PartSellingFactor:number,
   PartPartDescription:string,
   SerialMaskMaskType:number,
   SerialMaskMask:string,
   SerialMaskExample:string,
   SerialMaskDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SelectSerialNumbersParamsRow{
      /**  The part number to which the serial numbers have been assigned.  */  
   partNum:string,
      /**  The quantity of serial numbers that need to be selected.  */  
   quantity:number,
      /**  whereClause for filtering available serial numbers  */  
   whereClause:string,
      /**  transType of this transaction  */  
   transType:string,
      /**  Include when filtering a set of SN's for BL processing is necessary.  It may be null if not needed.  */  
   sourceRowID:string,
      /**  Determines if serial numbers can be created.  */  
   enableCreate:boolean,
      /**  Determines if serial numbers can be selected.  */  
   enableSelect:boolean,
      /**  Determines if serial numbers can be retrieved.  */  
   enableRetrieve:boolean,
      /**  Specifies whether Voided serial numbers can be manually selected.  */  
   allowVoided:boolean,
      /**  The Plant associated with this transaction  */  
   plant:string,
   xrefPartNum:string,
   xrefPartType:string,
   xrefCustNum:number,
      /**  temporary field used to link the packout lines to ship detail lines  */  
   poLinkValues:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   attributeSetID:number,
      /**  The Short Description of the Attribute Set.  */  
   attributeSetShortDescription:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   revisionNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SelectSerialNumbersParamsTableset{
   SelectSerialNumbersParams:Erp_Tablesets_SelectSerialNumbersParamsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_SelectedSerialNumbersRow{
      /**  Company  */  
   Company:string,
      /**  SerialNumber  */  
   SerialNumber:string,
      /**  Scrapped flag  */  
   Scrapped:boolean,
      /**  Scrapped reason code  */  
   ScrappedReasonCode:string,
      /**  Voided flag  */  
   Voided:boolean,
      /**  Reference field  */  
   Reference:string,
      /**  Reason code type = s  */  
   ReasonCodeType:string,
      /**  Reason code description  */  
   ReasonCodeDesc:string,
      /**  PartNumber  */  
   PartNum:string,
      /**  Serial number prefix  */  
   SNPrefix:string,
      /**  Base number used to create the serial number  */  
   SNBaseNumber:string,
      /**  RowID of the source record for this serial number  */  
   SourceRowID:string,
      /**  TransType of the record that created this serial number  */  
   TransType:string,
      /**  True if this serial numbered part passed inspection  */  
   PassedInspection:boolean,
      /**  Used to flag previously selected serial numbers as deselected  */  
   Deselected:boolean,
   KitWhseList:string,
      /**  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a validate type mask was being used where characters were stripped (using ~ in the mask).  */  
   RawSerialNum:string,
      /**  Action type field used for Kanban receipts to indicate if the new serial number status is Inventory, Scrapped or NonConf.  This requires Code/desc:  1 ` inventory 2 ` Scrapped 3 ` Nonconformance  */  
   KBLbrAction:number,
      /**  Description field for KBLbrAction ? holds the translated description for the KBLbrAction code for UI display and combo box.  */  
   KBLbrActionDesc:string,
      /**  If true, then users can not deselect this serial number.  This is used by applications that allow maintenance to the Selected Serial Numbers after update.  */  
   PreventDeselect:boolean,
      /**  Used only by SN Assignment  */  
   XRefPartNum:string,
      /**  Used only by SN Assignment: C = Customer Part / I = Internal Part XRef  */  
   XRefPartType:string,
   PreDeselected:boolean,
      /**  temporary field used to link the packout lines to ship detail lines  */  
   poLinkValues:string,
      /**  The mask the was used to generate the serial number  */  
   SNMask:string,
      /**  Flag to indicate that the SelectedSerialNumbers entry has not yet been saved to the DB for the related transaction. Used to keep track of which deselected serial numbers need to be passed to the transaction update logic.  */  
   NotSavedToDB:boolean,
   RowSelected:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtNonConfTableset{
   NonConf:Erp_Tablesets_NonConfRow[],
   NonConfAttch:Erp_Tablesets_NonConfAttchRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   SelectedSerialNumbers:Erp_Tablesets_SelectedSerialNumbersRow[],
   SNFormat:Erp_Tablesets_SNFormatRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface GetAvailTranDocTypes_output{
parameters : {
      /**  output parameters  */  
   listAvailTranDocTypes:string,
}
}

   /** Required : 
      @param ds
   */  
export interface GetAvailableQty_input{
   ds:Erp_Tablesets_NonConfTableset[],
}

export interface GetAvailableQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NonConfTableset[],
}
}

   /** Required : 
      @param tranID
   */  
export interface GetByID_input{
   tranID:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_NonConfTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_NonConfTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_NonConfTableset[],
}

   /** Required : 
      @param tableName
      @param fieldName
   */  
export interface GetCodeDescList_input{
   tableName:string,
   fieldName:string,
}

export interface GetCodeDescList_output{
   returnObj:string,
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
   returnObj:Erp_Tablesets_NonConfListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param company
      @param nonConfTranID
      @param tranType
   */  
export interface GetMtlQueueSeqValue_input{
   company:string,
   nonConfTranID:number,
   tranType:string,
}

export interface GetMtlQueueSeqValue_output{
   returnObj:number,
}

   /** Required : 
      @param pcJobNum
      @param piAssemblySeq
      @param piMtlSeq
   */  
export interface GetMtlSources_input{
      /**  Job number of the Job Material.  */  
   pcJobNum:string,
      /**  Job Assembly Sequence of the Job Material.  */  
   piAssemblySeq:number,
      /**  Material Sequence of the Job Material.  */  
   piMtlSeq:number,
}

export interface GetMtlSources_output{
   returnObj:Erp_Tablesets_NonConfSourceTableset[],
parameters : {
      /**  output parameters  */  
   pcMtlSourceTrnType:string,
}
}

   /** Required : 
      @param ds
      @param tranID
   */  
export interface GetNewNonConfAttch_input{
   ds:Erp_Tablesets_NonConfTableset[],
   tranID:number,
}

export interface GetNewNonConfAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NonConfTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewNonConf_input{
   ds:Erp_Tablesets_NonConfTableset[],
}

export interface GetNewNonConf_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NonConfTableset[],
}
}

   /** Required : 
      @param pcPartNum
   */  
export interface GetPartInfo_input{
      /**  Part Number.  */  
   pcPartNum:string,
}

export interface GetPartInfo_output{
parameters : {
      /**  output parameters  */  
   pcRevisionNum:string,
   pcUM:string,
   pcWarehouseCode:string,
   plLotTracked:boolean,
   plDimTracked:boolean,
   pcWareHseCodeDesc:string,
   pcBinNum:string,
}
}

   /** Required : 
      @param tranID
   */  
export interface GetPartTranPKs_input{
      /**  NonConf.TranID.  */  
   tranID:number,
}

export interface GetPartTranPKs_output{
parameters : {
      /**  output parameters  */  
   partTranPKs:string,
}
}

   /** Required : 
      @param pcNonConfType
   */  
export interface GetReasonWhereClause_input{
      /**  Type/origin of NonConformance.  */  
   pcNonConfType:string,
}

export interface GetReasonWhereClause_output{
      /**  WHERE clause suitable for use with Reason.GetList()  */  
   returnObj:string,
}

   /** Required : 
      @param whereClauseNonConf
      @param whereClauseNonConfAttch
      @param whereClauseLegalNumGenOpts
      @param whereClauseSelectedSerialNumbers
      @param whereClauseSNFormat
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseNonConf:string,
   whereClauseNonConfAttch:string,
   whereClauseLegalNumGenOpts:string,
   whereClauseSelectedSerialNumbers:string,
   whereClauseSNFormat:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_NonConfTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param serialControlPlantIsFromPlt
      @param serialControlPlant
      @param serialControlPlant2
      @param snIsEnabled
      @param partNum
      @param attributeSetID
      @param BinNum
      @param warehouseCode
      @param jobNum
      @param assemblySeq
      @param quantity
      @param scrapUM
      @param tranUOM
      @param sourceRowID
      @param pcProcessID
      @param trnTyp
      @param materialSeq
   */  
export interface GetSelectSerialNumbersParams_input{
      /**  Indicates if the from plant is controlling the serial processing (UI Application).  */  
   serialControlPlantIsFromPlt:boolean,
      /**  The plant that is controlling serial behavior for the transaction(UI Application).  */  
   serialControlPlant:string,
      /**  The to plant for the transaction if from plant is controlling (UI Application).  */  
   serialControlPlant2:string,
      /**  Indicates if the transaction requires serial number selection (UI Application).  */  
   snIsEnabled:boolean,
      /**  The part number for the transaction(UI Application).  */  
   partNum:string,
      /**  The part attribute set  */  
   attributeSetID:number,
      /**  The bin for the transaction(UI Application).  */  
   BinNum:string,
      /**  The warehouse for the transaction(UI Application).  */  
   warehouseCode:string,
      /**  The job for the transaction(UI Application).  */  
   jobNum:string,
      /**  The assembly for the transaction(UI Application).  */  
   assemblySeq:string,
      /**  The quantity for the transaction(UI Application).  */  
   quantity:number,
      /**  The unit of measure for the transaction(UI Application).  */  
   scrapUM:string,
      /**  The the converted UOM for the transaction(UI Application).  */  
   tranUOM:string,
      /**  The RowIdent of the NonConf line for the transaction(UI Application).  */  
   sourceRowID:string,
      /**  The name of the calling process (UI Application).  */  
   pcProcessID:string,
      /**  The name of the calling process (UI Application).  */  
   trnTyp:string,
      /**  The Material Sequence for the transaction.  */  
   materialSeq:number,
}

export interface GetSelectSerialNumbersParams_output{
   returnObj:Erp_Tablesets_SelectSerialNumbersParamsTableset[],
}

   /** Required : 
      @param processID
      @param ds
   */  
export interface GetSelectedSerialNumbersParams_input{
   processID:string,
   ds:Erp_Tablesets_NonConfTableset[],
}

export interface GetSelectedSerialNumbersParams_output{
   returnObj:Erp_Tablesets_SelectSerialNumbersParamsTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NonConfTableset[],
}
}

   /** Required : 
      @param pcNonConfRowIdent
      @param snIsEnabled
      @param serialControlPlant
      @param ds
   */  
export interface GetSelectedSerialNumbers_input{
      /**  Input RowIdent field of NonConf datatable  */  
   pcNonConfRowIdent:string,
      /**  Indicates if serial numbers are requied for the NonConf line  */  
   snIsEnabled:boolean,
      /**  The plant that is controlling the serial behavior for the NonConf line  */  
   serialControlPlant:string,
   ds:Erp_Tablesets_NonConfTableset[],
}

export interface GetSelectedSerialNumbers_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NonConfTableset[],
}
}

   /** Required : 
      @param pcPartNum
   */  
export interface Get_PartRev_input{
      /**  Part Number.  */  
   pcPartNum:string,
}

export interface Get_PartRev_output{
parameters : {
      /**  output parameters  */  
   pcRevisionNum:string,
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
      @param pcPartNum
      @param pcWhseCode
      @param pcBinNum
      @param pcLotNum
      @param pcAttributeSetID
      @param pcPCID
      @param pcDimCode
      @param pdDimConvFactor
      @param ipSellingQuantity
   */  
export interface NegativeInventoryTest_input{
   pcPartNum:string,
   pcWhseCode:string,
   pcBinNum:string,
   pcLotNum:string,
   pcAttributeSetID:number,
   pcPCID:string,
   pcDimCode:string,
   pdDimConvFactor:number,
   ipSellingQuantity:number,
}

export interface NegativeInventoryTest_output{
parameters : {
      /**  output parameters  */  
   pcNeqQtyAction:string,
   pcMessage:string,
}
}

   /** Required : 
      @param pBin
      @param lfrom
      @param ds
   */  
export interface OnChangeBinNum_input{
      /**  Bin Number  */  
   pBin:string,
      /**  Bool indicating to or from bin  */  
   lfrom:boolean,
   ds:Erp_Tablesets_NonConfTableset[],
}

export interface OnChangeBinNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NonConfTableset[],
}
}

   /** Required : 
      @param pcid
      @param pCallProcess
      @param ds
   */  
export interface OnChangeFromPCID_input{
   pcid:string,
   pCallProcess:string,
   ds:Erp_Tablesets_NonConfTableset[],
}

export interface OnChangeFromPCID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NonConfTableset[],
}
}

   /** Required : 
      @param piProposedAssemblySeq
      @param ds
   */  
export interface OnChangeJobAsm_input{
      /**  The new proposed Job Assembly value  */  
   piProposedAssemblySeq:number,
   ds:Erp_Tablesets_NonConfTableset[],
}

export interface OnChangeJobAsm_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NonConfTableset[],
}
}

   /** Required : 
      @param piProposedMtlSeq
      @param ds
   */  
export interface OnChangeJobMtl_input{
      /**  The new proposed Job Material value  */  
   piProposedMtlSeq:number,
   ds:Erp_Tablesets_NonConfTableset[],
}

export interface OnChangeJobMtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NonConfTableset[],
}
}

   /** Required : 
      @param pcProposedJobNum
      @param ds
   */  
export interface OnChangeJobNum_input{
      /**  The new proposed JobNum value  */  
   pcProposedJobNum:string,
   ds:Erp_Tablesets_NonConfTableset[],
}

export interface OnChangeJobNum_output{
parameters : {
      /**  output parameters  */  
   plAsmReturned:boolean,
   snWarning:string,
   ds:Erp_Tablesets_NonConfTableset[],
}
}

   /** Required : 
      @param piProposedOprSeq
      @param lNCOpr
      @param ds
   */  
export interface OnChangeJobOpr_input{
      /**  The new proposed Job Operation Sequence value  */  
   piProposedOprSeq:number,
      /**  Boolean. true = nonconfroming Operation, false = reporting Operation  */  
   lNCOpr:boolean,
   ds:Erp_Tablesets_NonConfTableset[],
}

export interface OnChangeJobOpr_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NonConfTableset[],
}
}

   /** Required : 
      @param pcid
      @param pCallProcess
      @param ds
   */  
export interface OnChangeToPCID_input{
   pcid:string,
   pCallProcess:string,
   ds:Erp_Tablesets_NonConfTableset[],
}

export interface OnChangeToPCID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NonConfTableset[],
}
}

   /** Required : 
      @param pdTranQty
      @param ds
   */  
export interface OnChangeTranQty_input{
      /**  Transaction Qty  */  
   pdTranQty:number,
   ds:Erp_Tablesets_NonConfTableset[],
}

export interface OnChangeTranQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NonConfTableset[],
}
}

   /** Required : 
      @param pUM
      @param ds
   */  
export interface OnChangeUM_input{
      /**  Transaction UOM  */  
   pUM:string,
   ds:Erp_Tablesets_NonConfTableset[],
}

export interface OnChangeUM_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NonConfTableset[],
}
}

   /** Required : 
      @param pWhse
      @param lfrom
      @param ds
   */  
export interface OnChangeWarehouseCode_input{
      /**  Warehouse Code  */  
   pWhse:string,
      /**  Bool indicating to or from warehouse  */  
   lfrom:boolean,
   ds:Erp_Tablesets_NonConfTableset[],
}

export interface OnChangeWarehouseCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NonConfTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangedCOPartNum_input{
   ds:Erp_Tablesets_NonConfTableset[],
}

export interface OnChangedCOPartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NonConfTableset[],
}
}

   /** Required : 
      @param attributeSetID
      @param ds
   */  
export interface OnChangingAttributeSet_input{
   attributeSetID:number,
   ds:Erp_Tablesets_NonConfTableset[],
}

export interface OnChangingAttributeSet_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NonConfTableset[],
}
}

   /** Required : 
      @param revisionNum
      @param ds
   */  
export interface OnChangingRevisionNum_input{
   revisionNum:string,
   ds:Erp_Tablesets_NonConfTableset[],
}

export interface OnChangingRevisionNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NonConfTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface PreUpdate_input{
   ds:Erp_Tablesets_NonConfTableset[],
}

export interface PreUpdate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NonConfTableset[],
   requiresUserInput:boolean,
   whBinWarning:string,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtNonConfTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtNonConfTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_NonConfTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NonConfTableset[],
}
}

   /** Required : 
      @param pcPartNum
      @param pcWhseCode
      @param pcBinNum
      @param pcLotNum
      @param pcAttributeSetID
      @param pcPCID
      @param pcDimCode
      @param pdDimConvFactor
      @param ipSellingQuantity
   */  
export interface ValidateQtyInventoryTestIncludingPCID_input{
   pcPartNum:string,
   pcWhseCode:string,
   pcBinNum:string,
   pcLotNum:string,
   pcAttributeSetID:number,
   pcPCID:string,
   pcDimCode:string,
   pdDimConvFactor:number,
   ipSellingQuantity:number,
}

export interface ValidateQtyInventoryTestIncludingPCID_output{
parameters : {
      /**  output parameters  */  
   pcNeqQtyAction:string,
   pcMessage:string,
}
}

   /** Required : 
      @param pcPartNum
      @param pcWhseCode
      @param pcBinNum
      @param pcLotNum
      @param pcAttributeSetID
      @param pcDimCode
      @param pdDimConvFactor
      @param ipSellingQuantity
      @param tran
   */  
export interface ValidateQtyInventoryTest_input{
   pcPartNum:string,
   pcWhseCode:string,
   pcBinNum:string,
   pcLotNum:string,
   pcAttributeSetID:number,
   pcDimCode:string,
   pdDimConvFactor:number,
   ipSellingQuantity:number,
   tran:number,
}

export interface ValidateQtyInventoryTest_output{
parameters : {
      /**  output parameters  */  
   pcNeqQtyAction:string,
   pcMessage:string,
}
}

   /** Required : 
      @param ds
      @param serialNumber
   */  
export interface ValidateSN_input{
   ds:Erp_Tablesets_NonConfTableset[],
      /**  Serial number to validate.  */  
   serialNumber:string,
}

export interface ValidateSN_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NonConfTableset[],
   isVoided:boolean,
}
}

