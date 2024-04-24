import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.TaxResultsSvc
// Description: This object does not have update capabilities
Only record retreival is available.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxResultsSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxResultsSvc/$metadata", {
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
   Description: Get TaxResults items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaxResults
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxSvcHeadRow
   */  
export function get_TaxResults(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxSvcHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxResultsSvc/TaxResults", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxSvcHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaxResults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaxSvcHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaxSvcHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TaxResults(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxResultsSvc/TaxResults", {
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
   Summary: Calls GetByID to retrieve the TaxResult item
   Description: Calls GetByID to retrieve the TaxResult item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxResult
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxSvcID Desc: TaxSvcID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxSvcHeadRow
   */  
export function get_TaxResults_Company_TaxSvcID(Company:string, TaxSvcID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TaxSvcHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxResultsSvc/TaxResults(" + Company + "," + TaxSvcID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_TaxSvcHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update TaxResult for the service
   Description: Calls UpdateExt to update TaxResult. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaxResult
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxSvcID Desc: TaxSvcID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaxSvcHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_TaxResults_Company_TaxSvcID(Company:string, TaxSvcID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxResultsSvc/TaxResults(" + Company + "," + TaxSvcID + ")", {
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
   Summary: Call UpdateExt to delete TaxResult item
   Description: Call UpdateExt to delete TaxResult item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaxResult
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxSvcID Desc: TaxSvcID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_TaxResults_Company_TaxSvcID(Company:string, TaxSvcID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxResultsSvc/TaxResults(" + Company + "," + TaxSvcID + ")", {
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
   Description: Get TaxSvcDetails items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TaxSvcDetails1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxSvcID Desc: TaxSvcID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxSvcDetailRow
   */  
export function get_TaxResults_Company_TaxSvcID_TaxSvcDetails(Company:string, TaxSvcID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxSvcDetailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxResultsSvc/TaxResults(" + Company + "," + TaxSvcID + ")/TaxSvcDetails", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxSvcDetailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the TaxSvcDetail item
   Description: Calls GetByID to retrieve the TaxSvcDetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxSvcDetail1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxSvcID Desc: TaxSvcID   Required: True   Allow empty value : True
      @param TCNo Desc: TCNo   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxSvcDetailRow
   */  
export function get_TaxResults_Company_TaxSvcID_TaxSvcDetails_Company_TaxSvcID_TCNo(Company:string, TaxSvcID:string, TCNo:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TaxSvcDetailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxResultsSvc/TaxResults(" + Company + "," + TaxSvcID + ")/TaxSvcDetails(" + Company + "," + TaxSvcID + "," + TCNo + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_TaxSvcDetailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get TaxSvcMessages items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TaxSvcMessages1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxSvcID Desc: TaxSvcID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxSvcMessagesRow
   */  
export function get_TaxResults_Company_TaxSvcID_TaxSvcMessages(Company:string, TaxSvcID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxSvcMessagesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxResultsSvc/TaxResults(" + Company + "," + TaxSvcID + ")/TaxSvcMessages", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxSvcMessagesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the TaxSvcMessage item
   Description: Calls GetByID to retrieve the TaxSvcMessage item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxSvcMessage1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxSvcID Desc: TaxSvcID   Required: True   Allow empty value : True
      @param Sequence Desc: Sequence   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxSvcMessagesRow
   */  
export function get_TaxResults_Company_TaxSvcID_TaxSvcMessages_Company_TaxSvcID_Sequence(Company:string, TaxSvcID:string, Sequence:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TaxSvcMessagesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxResultsSvc/TaxResults(" + Company + "," + TaxSvcID + ")/TaxSvcMessages(" + Company + "," + TaxSvcID + "," + Sequence + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_TaxSvcMessagesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get TaxSvcDetails items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaxSvcDetails
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxSvcDetailRow
   */  
export function get_TaxSvcDetails(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxSvcDetailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxResultsSvc/TaxSvcDetails", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxSvcDetailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaxSvcDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaxSvcDetailRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaxSvcDetailRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TaxSvcDetails(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxResultsSvc/TaxSvcDetails", {
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
   Summary: Calls GetByID to retrieve the TaxSvcDetail item
   Description: Calls GetByID to retrieve the TaxSvcDetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxSvcDetail
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxSvcID Desc: TaxSvcID   Required: True   Allow empty value : True
      @param TCNo Desc: TCNo   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxSvcDetailRow
   */  
export function get_TaxSvcDetails_Company_TaxSvcID_TCNo(Company:string, TaxSvcID:string, TCNo:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TaxSvcDetailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxResultsSvc/TaxSvcDetails(" + Company + "," + TaxSvcID + "," + TCNo + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_TaxSvcDetailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update TaxSvcDetail for the service
   Description: Calls UpdateExt to update TaxSvcDetail. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaxSvcDetail
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxSvcID Desc: TaxSvcID   Required: True   Allow empty value : True
      @param TCNo Desc: TCNo   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaxSvcDetailRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_TaxSvcDetails_Company_TaxSvcID_TCNo(Company:string, TaxSvcID:string, TCNo:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxResultsSvc/TaxSvcDetails(" + Company + "," + TaxSvcID + "," + TCNo + ")", {
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
   Summary: Call UpdateExt to delete TaxSvcDetail item
   Description: Call UpdateExt to delete TaxSvcDetail item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaxSvcDetail
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxSvcID Desc: TaxSvcID   Required: True   Allow empty value : True
      @param TCNo Desc: TCNo   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_TaxSvcDetails_Company_TaxSvcID_TCNo(Company:string, TaxSvcID:string, TCNo:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxResultsSvc/TaxSvcDetails(" + Company + "," + TaxSvcID + "," + TCNo + ")", {
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
   Description: Get TaxSvcJurDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TaxSvcJurDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxSvcID Desc: TaxSvcID   Required: True   Allow empty value : True
      @param TCNo Desc: TCNo   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxSvcJurDtlRow
   */  
export function get_TaxSvcDetails_Company_TaxSvcID_TCNo_TaxSvcJurDtls(Company:string, TaxSvcID:string, TCNo:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxSvcJurDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxResultsSvc/TaxSvcDetails(" + Company + "," + TaxSvcID + "," + TCNo + ")/TaxSvcJurDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxSvcJurDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the TaxSvcJurDtl item
   Description: Calls GetByID to retrieve the TaxSvcJurDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxSvcJurDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxSvcID Desc: TaxSvcID   Required: True   Allow empty value : True
      @param TCNo Desc: TCNo   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxSvcJurDtlRow
   */  
export function get_TaxSvcDetails_Company_TaxSvcID_TCNo_TaxSvcJurDtls_Company_TaxSvcID_TCNo_Seq(Company:string, TaxSvcID:string, TCNo:string, Seq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TaxSvcJurDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxResultsSvc/TaxSvcDetails(" + Company + "," + TaxSvcID + "," + TCNo + ")/TaxSvcJurDtls(" + Company + "," + TaxSvcID + "," + TCNo + "," + Seq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_TaxSvcJurDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get TaxSvcJurDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaxSvcJurDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxSvcJurDtlRow
   */  
export function get_TaxSvcJurDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxSvcJurDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxResultsSvc/TaxSvcJurDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxSvcJurDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaxSvcJurDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaxSvcJurDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaxSvcJurDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TaxSvcJurDtls(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxResultsSvc/TaxSvcJurDtls", {
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
   Summary: Calls GetByID to retrieve the TaxSvcJurDtl item
   Description: Calls GetByID to retrieve the TaxSvcJurDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxSvcJurDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxSvcID Desc: TaxSvcID   Required: True   Allow empty value : True
      @param TCNo Desc: TCNo   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxSvcJurDtlRow
   */  
export function get_TaxSvcJurDtls_Company_TaxSvcID_TCNo_Seq(Company:string, TaxSvcID:string, TCNo:string, Seq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TaxSvcJurDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxResultsSvc/TaxSvcJurDtls(" + Company + "," + TaxSvcID + "," + TCNo + "," + Seq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_TaxSvcJurDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update TaxSvcJurDtl for the service
   Description: Calls UpdateExt to update TaxSvcJurDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaxSvcJurDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxSvcID Desc: TaxSvcID   Required: True   Allow empty value : True
      @param TCNo Desc: TCNo   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaxSvcJurDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_TaxSvcJurDtls_Company_TaxSvcID_TCNo_Seq(Company:string, TaxSvcID:string, TCNo:string, Seq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxResultsSvc/TaxSvcJurDtls(" + Company + "," + TaxSvcID + "," + TCNo + "," + Seq + ")", {
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
   Summary: Call UpdateExt to delete TaxSvcJurDtl item
   Description: Call UpdateExt to delete TaxSvcJurDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaxSvcJurDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxSvcID Desc: TaxSvcID   Required: True   Allow empty value : True
      @param TCNo Desc: TCNo   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_TaxSvcJurDtls_Company_TaxSvcID_TCNo_Seq(Company:string, TaxSvcID:string, TCNo:string, Seq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxResultsSvc/TaxSvcJurDtls(" + Company + "," + TaxSvcID + "," + TCNo + "," + Seq + ")", {
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
   Description: Get TaxSvcMessages items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaxSvcMessages
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxSvcMessagesRow
   */  
export function get_TaxSvcMessages(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxSvcMessagesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxResultsSvc/TaxSvcMessages", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxSvcMessagesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaxSvcMessages
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaxSvcMessagesRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaxSvcMessagesRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TaxSvcMessages(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxResultsSvc/TaxSvcMessages", {
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
   Summary: Calls GetByID to retrieve the TaxSvcMessage item
   Description: Calls GetByID to retrieve the TaxSvcMessage item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxSvcMessage
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxSvcID Desc: TaxSvcID   Required: True   Allow empty value : True
      @param Sequence Desc: Sequence   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxSvcMessagesRow
   */  
export function get_TaxSvcMessages_Company_TaxSvcID_Sequence(Company:string, TaxSvcID:string, Sequence:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TaxSvcMessagesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxResultsSvc/TaxSvcMessages(" + Company + "," + TaxSvcID + "," + Sequence + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_TaxSvcMessagesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update TaxSvcMessage for the service
   Description: Calls UpdateExt to update TaxSvcMessage. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaxSvcMessage
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxSvcID Desc: TaxSvcID   Required: True   Allow empty value : True
      @param Sequence Desc: Sequence   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaxSvcMessagesRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_TaxSvcMessages_Company_TaxSvcID_Sequence(Company:string, TaxSvcID:string, Sequence:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxResultsSvc/TaxSvcMessages(" + Company + "," + TaxSvcID + "," + Sequence + ")", {
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
   Summary: Call UpdateExt to delete TaxSvcMessage item
   Description: Call UpdateExt to delete TaxSvcMessage item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaxSvcMessage
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxSvcID Desc: TaxSvcID   Required: True   Allow empty value : True
      @param Sequence Desc: Sequence   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_TaxSvcMessages_Company_TaxSvcID_Sequence(Company:string, TaxSvcID:string, Sequence:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxResultsSvc/TaxSvcMessages(" + Company + "," + TaxSvcID + "," + Sequence + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxSvcHeadListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxSvcHeadListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxResultsSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxSvcHeadListRow)
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
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseTaxSvcHead:string, whereClauseTaxSvcDetail:string, whereClauseTaxSvcJurDtl:string, whereClauseTaxSvcMessages:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseTaxSvcHead!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseTaxSvcHead=" + whereClauseTaxSvcHead
   }
   if(typeof whereClauseTaxSvcDetail!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseTaxSvcDetail=" + whereClauseTaxSvcDetail
   }
   if(typeof whereClauseTaxSvcJurDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseTaxSvcJurDtl=" + whereClauseTaxSvcJurDtl
   }
   if(typeof whereClauseTaxSvcMessages!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseTaxSvcMessages=" + whereClauseTaxSvcMessages
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxResultsSvc/GetRows" + params, {
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
export function get_GetByID(taxSvcID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof taxSvcID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "taxSvcID=" + taxSvcID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxResultsSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxResultsSvc/GetList" + params, {
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
   Summary: Invoke method GetTaxSvcID
   Description: this method returns TaxSvcID field
   OperationID: GetTaxSvcID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTaxSvcID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTaxSvcID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTaxSvcID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxResultsSvc/GetTaxSvcID", {
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
   Summary: Invoke method GetVendorTaxSvcID
   Description: Calculate TaxSvcID for ap invoice.
   OperationID: GetVendorTaxSvcID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetVendorTaxSvcID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVendorTaxSvcID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetVendorTaxSvcID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxResultsSvc/GetVendorTaxSvcID", {
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
   Summary: Invoke method GetNewTaxSvcHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTaxSvcHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTaxSvcHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaxSvcHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewTaxSvcHead(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxResultsSvc/GetNewTaxSvcHead", {
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
   Summary: Invoke method GetNewTaxSvcDetail
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTaxSvcDetail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTaxSvcDetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaxSvcDetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewTaxSvcDetail(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxResultsSvc/GetNewTaxSvcDetail", {
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
   Summary: Invoke method GetNewTaxSvcJurDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTaxSvcJurDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTaxSvcJurDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaxSvcJurDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewTaxSvcJurDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxResultsSvc/GetNewTaxSvcJurDtl", {
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
   Summary: Invoke method GetNewTaxSvcMessages
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTaxSvcMessages
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTaxSvcMessages_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaxSvcMessages_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewTaxSvcMessages(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxResultsSvc/GetNewTaxSvcMessages", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxResultsSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxResultsSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxResultsSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxResultsSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxResultsSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxSvcDetailRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TaxSvcDetailRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxSvcHeadListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TaxSvcHeadListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxSvcHeadRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TaxSvcHeadRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxSvcJurDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TaxSvcJurDtlRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxSvcMessagesRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TaxSvcMessagesRow[],
}

export interface Erp_Tablesets_TaxSvcDetailRow{
      /**  Company Identifier  */  
   "Company":string,
      /**  'Type + - (OrderNum, InvoiceNum,  QuoteNum or TCDocID)'. Depending on the type, where Type is O=order, Q = quote, I = invoice, T=tax service doc ID (this is used to create an TaxSvcHead for tax reoconciliation when Tax Connect has a record with no corresponding Epicor record). Example: O-1234 is order type and order number 1234; Q-1234 is quote type and quote number 1234, etc.  */  
   "TaxSvcID":string,
      /**  Link to Sales Order  */  
   "OrderNum":number,
      /**  Link to Invoice or Credit Memo  */  
   "InvoiceNum":number,
      /**  Invoice or Order Line Number  */  
   "LineNum":number,
      /**  For SO, the release number associated with this tax detail  */  
   "OrderRelNum":number,
      /**  Part number  */  
   "PartNum":string,
      /**  Quantity for this line item  */  
   "Quantity":number,
      /**  Price of this item  */  
   "UnitPrice":number,
      /**  Quantity x Unit Price  */  
   "ExtPrice":number,
      /**  Amount of this line item that can be taxec  */  
   "TaxableAmount":number,
      /**  Amount of tax for this line item  */  
   "TaxAmt":number,
      /**  Discount  */  
   "Discount":number,
      /**  Tax Category  */  
   "TaxCategory":string,
      /**  Address item was shipped from  */  
   "FromAddress1":string,
      /**  Address item was shipped from  */  
   "FromAddress2":string,
      /**  Address item was shipped from  */  
   "FromAddress3":string,
      /**  City item was shipped from  */  
   "FromCity":string,
      /**  State item was shipped from  */  
   "FromState":string,
      /**  Postal Code or zip code item was shipped from  */  
   "FromZip":string,
      /**  Country item was shipped from  */  
   "FromCountry":string,
      /**  Address item was shipped TO  */  
   "ToAddress1":string,
      /**  Address item was shipped to  */  
   "ToAddress2":string,
      /**  Address item was shipped to  */  
   "ToAddress3":string,
      /**  City item was shipped to  */  
   "ToCity":string,
      /**  State item was shipped to  */  
   "ToState":string,
      /**  Postal Code or zip code item was shipped to  */  
   "ToZip":string,
      /**  Country item was shipped to  */  
   "ToCountry":string,
      /**  Link to Quote  */  
   "QuoteNum":number,
      /**  Tax region used to compute taxes.  */  
   "TaxRegionCode":string,
      /**  Same as TaxSvcHead DocID. The unique id assigned by the tax service in GetTax or ReconcileTaxHistory call. Used to match GetTax data with ReconcileTaxHistory data.  */  
   "DocID":number,
      /**  The line number that is used by Avalara for this TaxSvcDetail. It will consist of LineNum + OrderRelNum + a generated sequence number to keep the line number unique in Avalara. This is required because we send separate tax Line[] entries to GetTax for the line/release and each of its misc charge codes. In that case all of the line and release numbers are the same for GetTax on the line/release and misc charges, so we append a sequence counter unique to that line/release combination so we can properly sort the tax results.  */  
   "TCNo":string,
      /**  TaxLine.Rate from GetTax call  */  
   "TCRate":number,
      /**  TaxLine.Rate from GetTaxHistory call  */  
   "TCHRate":number,
      /**  TaxLine.Tax from GetTax call  */  
   "TCTax":number,
      /**  TaxLine.Tax from GetTaxHistory call  */  
   "TCHTax":number,
      /**  TaxLine.Taxability from GetTax call  */  
   "TCTaxability":boolean,
      /**  TaxLine.Taxability from GetTaxHistory call  */  
   "TCHTaxability":boolean,
      /**  TaxLine.Taxable from GetTax call  */  
   "TCTaxable":number,
      /**  TaxLine.Taxable from GetTaxHistory call  */  
   "TCHTaxable":number,
      /**  TaxLine.TaxCode from GetTax call  */  
   "TCTaxCode":string,
      /**  TaxLine.TaxCode from GetTaxHistory call  */  
   "TCHTaxCode":string,
      /**  The ItemSeq used when generating the value for the third sector of TaxSvcDetail TCNo.  */  
   "ItemSeq":number,
      /**  AP Invoice Number sent to Tax Connect  */  
   "APInvoiceNum":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "TaxCategoryDescription":string,
   "TaxRgnDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_TaxSvcHeadListRow{
      /**  Company Identifier  */  
   "Company":string,
      /**  'Type + - (OrderNum, InvoiceNum,  QuoteNum or TCDocID)'. Depending on the type, where Type is O=order, Q = quote, I = invoice, T=tax service doc ID (this is used to create an TaxSvcHead for tax reoconciliation when Tax Connect has a record with no corresponding Epicor record). Example: O-1234 is order type and order number 1234; Q-1234 is quote type and quote number 1234, etc.  */  
   "TaxSvcID":string,
      /**  Link to Sales Orders  */  
   "OrderNum":number,
      /**  Link to Invoice or Credit Memo  */  
   "InvoiceNum":number,
      /**  Document Date  */  
   "DocDate":string,
      /**  Customer number  */  
   "CustNum":number,
      /**  Doc Code passed to the GetTax function. Can represent an AR Invoice, AP Invoice or Sales Order.  */  
   "DocCodes":string,
      /**  Posted / Unposted  */  
   "DocState":string,
      /**  Saved / Posted / Committed / Cancelled  */  
   "RemoteState":string,
      /**  Sum of taxable amounts  */  
   "TotalAmount":number,
      /**  Sum of tax amounts  */  
   "TotalTax":number,
      /**  Sum of all line discounts  */  
   "TotalDiscount":number,
      /**  Indicates a reconciliation action has been executed by Perform Reconciliation for this TaxSvcHead. The action performed is in LastReconAction  */  
   "Reconciled":boolean,
      /**  SalesOrder = 0, SalesInvoice = 1, ReturnInvoice = 5  */  
   "DocType":number,
      /**  The unique id assigned by the tax service. Returned by the tax service.  */  
   "DocID":number,
      /**  Designates the document currency display symbol for the Epicor invoice Doc currency code  */  
   "DocDisplaySymbol":string,
      /**  Link to Quote  */  
   "QuoteNum":number,
      /**  The date the TaxSvcHead entry was created  */  
   "DateCreated":string,
      /**  The time this entry was created.  */  
   "TimeCreated":number,
      /**  DocDate from ReconcileTaxHistory call  */  
   "TCHDocCode":string,
      /**   DocStatus from ReconcileTaxHistory call
Requires Code/Desc:
S = Saved
P = Posted
C = Committed
X = Cancelled  */  
   "TCHRemoteState":string,
      /**  TotalAmount from ReconcileTaxHistoryCall  */  
   "TCHTotalAmount":number,
      /**  TotalDiscount from ReconcileTaxHistory call  */  
   "TCHTotalDiscount":number,
      /**  TotalTax from ReconcileTaxHistory call.  */  
   "TCHTotalTax":number,
      /**   ResultCode returned by GetTax call.
Code/desc data.  Avalara will return a single code for each address validation request. Success = Operation Succeeded; Warning = Warnings occurred, operation succeeded, Error = Errors occured, operation failed; Exception = Unexpected exceptions occurred, operation failed.  */  
   "ResultCode":string,
      /**  DocDate from ReconcileTaxHistory call  */  
   "TCHDocDate":string,
      /**   Action to be performed by the Tax Reconciliation Perform Reconcile option. Code/Desc:
N= None, X=Cancel, C=Commit, P=Post, G=GetTax, PC=Post and commit  */  
   "Action":string,
      /**   Indicates the last reconciliation action that was performed by Perform Reconcilation for this TaxSvcHead. Needs code/desc:
N= None, X=Cancel, C=Commit, P=Post, G=GetTax, PC=Post and commit  */  
   "LastReconAction":string,
      /**  AP Invoice Number sent to Tax Connect  */  
   "APInvoiceNum":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Actions available for tax reconciliation. Delimited by list-delim and sublist-delim  */  
   "AvailableActionOptions":string,
      /**  ActionDescription  */  
   "ActionDescription":string,
   "LastReconActionDesc":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_TaxSvcHeadRow{
      /**  Company Identifier  */  
   "Company":string,
      /**  'Type + - (OrderNum, InvoiceNum,  QuoteNum or TCDocID)'. Depending on the type, where Type is O=order, Q = quote, I = invoice, T=tax service doc ID (this is used to create an TaxSvcHead for tax reoconciliation when Tax Connect has a record with no corresponding Epicor record). Example: O-1234 is order type and order number 1234; Q-1234 is quote type and quote number 1234, etc.  */  
   "TaxSvcID":string,
      /**  Link to Sales Orders  */  
   "OrderNum":number,
      /**  Link to Invoice or Credit Memo  */  
   "InvoiceNum":number,
      /**  Document Date  */  
   "DocDate":string,
      /**  Customer number  */  
   "CustNum":number,
      /**  Doc Code passed to the GetTax function. Can represent an AR Invoice, AP Invoice or Sales Order.  */  
   "DocCodes":string,
      /**  Posted / Unposted  */  
   "DocState":string,
      /**  Saved / Posted / Committed / Cancelled  */  
   "RemoteState":string,
      /**  Sum of taxable amounts  */  
   "TotalAmount":number,
      /**  Sum of tax amounts  */  
   "TotalTax":number,
      /**  Sum of all line discounts  */  
   "TotalDiscount":number,
      /**  Indicates a reconciliation action has been executed by Perform Reconciliation for this TaxSvcHead. The action performed is in LastReconAction  */  
   "Reconciled":boolean,
      /**  SalesOrder = 0, SalesInvoice = 1, ReturnInvoice = 5  */  
   "DocType":number,
      /**  The unique id assigned by the tax service. Returned by the tax service.  */  
   "DocID":number,
      /**  Designates the document currency display symbol for the Epicor invoice Doc currency code  */  
   "DocDisplaySymbol":string,
      /**  Link to Quote  */  
   "QuoteNum":number,
      /**  The date the TaxSvcHead entry was created  */  
   "DateCreated":string,
      /**  The time this entry was created.  */  
   "TimeCreated":number,
      /**  DocDate from ReconcileTaxHistory call  */  
   "TCHDocCode":string,
      /**   DocStatus from ReconcileTaxHistory call
Requires Code/Desc:
S = Saved
P = Posted
C = Committed
X = Cancelled  */  
   "TCHRemoteState":string,
      /**  TotalAmount from ReconcileTaxHistoryCall  */  
   "TCHTotalAmount":number,
      /**  TotalDiscount from ReconcileTaxHistory call  */  
   "TCHTotalDiscount":number,
      /**  TotalTax from ReconcileTaxHistory call.  */  
   "TCHTotalTax":number,
      /**   ResultCode returned by GetTax call.
Code/desc data.  Avalara will return a single code for each address validation request. Success = Operation Succeeded; Warning = Warnings occurred, operation succeeded, Error = Errors occured, operation failed; Exception = Unexpected exceptions occurred, operation failed.  */  
   "ResultCode":string,
      /**  DocDate from ReconcileTaxHistory call  */  
   "TCHDocDate":string,
      /**   Action to be performed by the Tax Reconciliation Perform Reconcile option. Code/Desc:
N= None, X=Cancel, C=Commit, P=Post, G=GetTax, PC=Post and commit  */  
   "Action":string,
      /**   Indicates the last reconciliation action that was performed by Perform Reconcilation for this TaxSvcHead. Needs code/desc:
N= None, X=Cancel, C=Commit, P=Post, G=GetTax, PC=Post and commit  */  
   "LastReconAction":string,
      /**  AP Invoice Number sent to Tax Connect  */  
   "APInvoiceNum":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Actions available for tax reconciliation. Delimited by list-delim and sublist-delim  */  
   "AvailableActionOptions":string,
      /**  ActionDescription  */  
   "ActionDescription":string,
   "LastReconActionDesc":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_TaxSvcJurDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  'Type + - (OrderNum, InvoiceNum,  QuoteNum or TCDocID)'. Depending on the type, where Type is O=order, Q = quote, I = invoice, T=tax service doc ID (this is used to create an TaxSvcHead for tax reoconciliation when Tax Connect has a record with no corresponding Epicor record). Example: O-1234 is order type and order number 1234; Q-1234 is quote type and quote number 1234, etc.  */  
   "TaxSvcID":string,
      /**  Invoice, Quote or Order Line number  */  
   "LineNum":number,
      /**  For SO, the release number associated with this tax detail, for other types it will be zero.  */  
   "OrderRelNum":number,
      /**  Sequence to keep the key unique per TaxSvcID, LineNum, OrderRelNum because there can be multiple jurisdiction tax details for each document/Line/Release combination.  */  
   "Seq":number,
      /**  From TaxDetail Base, the taxable amount. In Doc currency.  */  
   "TaxableAmount":number,
      /**  Jurisdiction Code for the taxing jurisdiction from GetTax call  */  
   "JurisCode":string,
      /**  Jurisdiction name returned by GetTax call.  */  
   "JurisName":string,
      /**   Jurisdiction Type from GetTax call describes the jurisdiction for which a particular tax is applied to a document.
This needs Code/desc data  Avalara will return Composite = Unspecified Jurisdiction; State = State, County = County; City = City; Special = Special Tax Jurisdiction.  */  
   "JurisType":string,
      /**  The tax rate, i.e. the rate of taxation (0.0 - 1.0). From TaxDetail Rate returned by GetTax call  */  
   "Percent":number,
      /**  The tax amount, i.e. the calculated tax. From TaxDetail Tax in GetTax call. In Doc currency.  */  
   "TaxAmt":number,
      /**   TaxDetail.Tax type returned by GetTax call
This needs Code/desc data set up: Avalara will return S = Sales Tax; U = Use Tax.  */  
   "TaxType":string,
      /**  Same as TaxSvcHead DocID. The unique id assigned by the tax service in GetTax or ReconcileTaxHistory call. Used to match GetTax data with ReconcileTaxHistory data.  */  
   "DocID":number,
      /**  The line number that is used by Avalara for this TaxSvcDetail. It will consist of LineNum + OrderRelNum + a generated sequence number to keep the line number unique in Avalara. This is required because we send separate tax Line[] entries to GetTax for the line/release and each of its misc charge codes. In that case all of the line and release numbers are the same for GetTax on the line/release and misc charges, so we append a sequence counter unique to that line/release combination so we can properly sort the tax results.  */  
   "TCNo":string,
      /**  From TaxDetail Base, the taxable amount from GetTaxHistory call. In Doc currency.  */  
   "TCHTaxableAmount":number,
      /**  Jurisdiction Code for the taxing jurisdiction from GetTaxHistory call  */  
   "TCHJurisCode":string,
      /**  Jurisdiction name returned by GetTaxHistory call.  */  
   "TCHJurisName":string,
      /**   Jurisdiction Type from GetTaxHistory call.
This needs Code/desc data  Avalara will return Composite = Unspecified Jurisdiction; State = State, County = County; City = City; Special = Special Tax Jurisdiction.  */  
   "TCHJurisType":string,
      /**  The tax rate, i.e. the rate of taxation (0.0 - 1.0). From TaxDetail Rate returned by GetTaxHistory call  */  
   "TCHPercent":number,
      /**  The tax amount, i.e. the calculated tax. From TaxDetail Tax in GetTaxHistory call. In Doc currency.  */  
   "TCHTaxAmt":number,
      /**   TaxDetail.Tax type returned by GetTaxHistory call
This needs Code/desc data set up: Avalara will return S = Sales Tax; U = Use Tax.  */  
   "TCHTaxType":string,
      /**  The ItemSeq used when generating the value for the third sector of TaxSvcDetail TCNo.  */  
   "ItemSeq":number,
      /**  Quote number is an integer which is used to uniquely identify a quote within the system.  */  
   "QuoteNum":number,
      /**  When creating a new order the user is prompted for an order number.  */  
   "OrderNum":number,
      /**  Invoice number of the related invoice.  */  
   "InvoiceNum":number,
      /**  AP Invoice Number sent to Tax Connect  */  
   "APInvoiceNum":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_TaxSvcMessagesRow{
      /**  Company Identifier  */  
   "Company":string,
      /**  'Type + - (OrderNum or InvoiceNum or QuoteNum'. Depending on the type, where Type is O=order, Q = quote and I = invoice. Example: O-1234 is order type and order number 1234; Q-1234 is quote type and quote number 1234, etc. Used to link TaxSvcMessages to TaxSvcHead  */  
   "TaxSvcID":string,
      /**  Sequence of TaxSvcMessage  */  
   "Sequence":number,
      /**  Link to Sales Order  */  
   "OrderNum":number,
      /**  Link to Invoice  */  
   "InvoiceNum":number,
      /**  Line number of item of the invoice or sales order  */  
   "LineNum":number,
      /**  Line number of item in remote tax system  */  
   "DocLineNum":number,
      /**  Detail of the message  */  
   "Detail":string,
      /**  URL of help page for this messag  */  
   "HelpLink":string,
      /**  Success, Warning, Error, Exception  */  
   "Severity":string,
      /**  Summary of the message  */  
   "Summary":string,
      /**  Unique identifier in remote tax system  */  
   "DocID":number,
      /**  Name of the message  */  
   "Name":string,
      /**  The item the message is referring to  */  
   "RefersTo":string,
      /**  Source of the message  */  
   "Source":string,
      /**  Link to Quote  */  
   "QuoteNum":number,
      /**  For SO, the release number associated with the message.  */  
   "OrderRelNum":number,
      /**  AP Invoice Number sent to Tax Connect  */  
   "APInvoiceNum":string,
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
      @param taxSvcID
   */  
export interface DeleteByID_input{
   taxSvcID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_TaxResultsTableset{
   TaxSvcHead:Erp_Tablesets_TaxSvcHeadRow[],
   TaxSvcDetail:Erp_Tablesets_TaxSvcDetailRow[],
   TaxSvcJurDtl:Erp_Tablesets_TaxSvcJurDtlRow[],
   TaxSvcMessages:Erp_Tablesets_TaxSvcMessagesRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_TaxSvcDetailRow{
      /**  Company Identifier  */  
   Company:string,
      /**  'Type + - (OrderNum, InvoiceNum,  QuoteNum or TCDocID)'. Depending on the type, where Type is O=order, Q = quote, I = invoice, T=tax service doc ID (this is used to create an TaxSvcHead for tax reoconciliation when Tax Connect has a record with no corresponding Epicor record). Example: O-1234 is order type and order number 1234; Q-1234 is quote type and quote number 1234, etc.  */  
   TaxSvcID:string,
      /**  Link to Sales Order  */  
   OrderNum:number,
      /**  Link to Invoice or Credit Memo  */  
   InvoiceNum:number,
      /**  Invoice or Order Line Number  */  
   LineNum:number,
      /**  For SO, the release number associated with this tax detail  */  
   OrderRelNum:number,
      /**  Part number  */  
   PartNum:string,
      /**  Quantity for this line item  */  
   Quantity:number,
      /**  Price of this item  */  
   UnitPrice:number,
      /**  Quantity x Unit Price  */  
   ExtPrice:number,
      /**  Amount of this line item that can be taxec  */  
   TaxableAmount:number,
      /**  Amount of tax for this line item  */  
   TaxAmt:number,
      /**  Discount  */  
   Discount:number,
      /**  Tax Category  */  
   TaxCategory:string,
      /**  Address item was shipped from  */  
   FromAddress1:string,
      /**  Address item was shipped from  */  
   FromAddress2:string,
      /**  Address item was shipped from  */  
   FromAddress3:string,
      /**  City item was shipped from  */  
   FromCity:string,
      /**  State item was shipped from  */  
   FromState:string,
      /**  Postal Code or zip code item was shipped from  */  
   FromZip:string,
      /**  Country item was shipped from  */  
   FromCountry:string,
      /**  Address item was shipped TO  */  
   ToAddress1:string,
      /**  Address item was shipped to  */  
   ToAddress2:string,
      /**  Address item was shipped to  */  
   ToAddress3:string,
      /**  City item was shipped to  */  
   ToCity:string,
      /**  State item was shipped to  */  
   ToState:string,
      /**  Postal Code or zip code item was shipped to  */  
   ToZip:string,
      /**  Country item was shipped to  */  
   ToCountry:string,
      /**  Link to Quote  */  
   QuoteNum:number,
      /**  Tax region used to compute taxes.  */  
   TaxRegionCode:string,
      /**  Same as TaxSvcHead DocID. The unique id assigned by the tax service in GetTax or ReconcileTaxHistory call. Used to match GetTax data with ReconcileTaxHistory data.  */  
   DocID:number,
      /**  The line number that is used by Avalara for this TaxSvcDetail. It will consist of LineNum + OrderRelNum + a generated sequence number to keep the line number unique in Avalara. This is required because we send separate tax Line[] entries to GetTax for the line/release and each of its misc charge codes. In that case all of the line and release numbers are the same for GetTax on the line/release and misc charges, so we append a sequence counter unique to that line/release combination so we can properly sort the tax results.  */  
   TCNo:string,
      /**  TaxLine.Rate from GetTax call  */  
   TCRate:number,
      /**  TaxLine.Rate from GetTaxHistory call  */  
   TCHRate:number,
      /**  TaxLine.Tax from GetTax call  */  
   TCTax:number,
      /**  TaxLine.Tax from GetTaxHistory call  */  
   TCHTax:number,
      /**  TaxLine.Taxability from GetTax call  */  
   TCTaxability:boolean,
      /**  TaxLine.Taxability from GetTaxHistory call  */  
   TCHTaxability:boolean,
      /**  TaxLine.Taxable from GetTax call  */  
   TCTaxable:number,
      /**  TaxLine.Taxable from GetTaxHistory call  */  
   TCHTaxable:number,
      /**  TaxLine.TaxCode from GetTax call  */  
   TCTaxCode:string,
      /**  TaxLine.TaxCode from GetTaxHistory call  */  
   TCHTaxCode:string,
      /**  The ItemSeq used when generating the value for the third sector of TaxSvcDetail TCNo.  */  
   ItemSeq:number,
      /**  AP Invoice Number sent to Tax Connect  */  
   APInvoiceNum:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   TaxCategoryDescription:string,
   TaxRgnDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TaxSvcHeadListRow{
      /**  Company Identifier  */  
   Company:string,
      /**  'Type + - (OrderNum, InvoiceNum,  QuoteNum or TCDocID)'. Depending on the type, where Type is O=order, Q = quote, I = invoice, T=tax service doc ID (this is used to create an TaxSvcHead for tax reoconciliation when Tax Connect has a record with no corresponding Epicor record). Example: O-1234 is order type and order number 1234; Q-1234 is quote type and quote number 1234, etc.  */  
   TaxSvcID:string,
      /**  Link to Sales Orders  */  
   OrderNum:number,
      /**  Link to Invoice or Credit Memo  */  
   InvoiceNum:number,
      /**  Document Date  */  
   DocDate:string,
      /**  Customer number  */  
   CustNum:number,
      /**  Doc Code passed to the GetTax function. Can represent an AR Invoice, AP Invoice or Sales Order.  */  
   DocCodes:string,
      /**  Posted / Unposted  */  
   DocState:string,
      /**  Saved / Posted / Committed / Cancelled  */  
   RemoteState:string,
      /**  Sum of taxable amounts  */  
   TotalAmount:number,
      /**  Sum of tax amounts  */  
   TotalTax:number,
      /**  Sum of all line discounts  */  
   TotalDiscount:number,
      /**  Indicates a reconciliation action has been executed by Perform Reconciliation for this TaxSvcHead. The action performed is in LastReconAction  */  
   Reconciled:boolean,
      /**  SalesOrder = 0, SalesInvoice = 1, ReturnInvoice = 5  */  
   DocType:number,
      /**  The unique id assigned by the tax service. Returned by the tax service.  */  
   DocID:number,
      /**  Designates the document currency display symbol for the Epicor invoice Doc currency code  */  
   DocDisplaySymbol:string,
      /**  Link to Quote  */  
   QuoteNum:number,
      /**  The date the TaxSvcHead entry was created  */  
   DateCreated:string,
      /**  The time this entry was created.  */  
   TimeCreated:number,
      /**  DocDate from ReconcileTaxHistory call  */  
   TCHDocCode:string,
      /**   DocStatus from ReconcileTaxHistory call
Requires Code/Desc:
S = Saved
P = Posted
C = Committed
X = Cancelled  */  
   TCHRemoteState:string,
      /**  TotalAmount from ReconcileTaxHistoryCall  */  
   TCHTotalAmount:number,
      /**  TotalDiscount from ReconcileTaxHistory call  */  
   TCHTotalDiscount:number,
      /**  TotalTax from ReconcileTaxHistory call.  */  
   TCHTotalTax:number,
      /**   ResultCode returned by GetTax call.
Code/desc data.  Avalara will return a single code for each address validation request. Success = Operation Succeeded; Warning = Warnings occurred, operation succeeded, Error = Errors occured, operation failed; Exception = Unexpected exceptions occurred, operation failed.  */  
   ResultCode:string,
      /**  DocDate from ReconcileTaxHistory call  */  
   TCHDocDate:string,
      /**   Action to be performed by the Tax Reconciliation Perform Reconcile option. Code/Desc:
N= None, X=Cancel, C=Commit, P=Post, G=GetTax, PC=Post and commit  */  
   Action:string,
      /**   Indicates the last reconciliation action that was performed by Perform Reconcilation for this TaxSvcHead. Needs code/desc:
N= None, X=Cancel, C=Commit, P=Post, G=GetTax, PC=Post and commit  */  
   LastReconAction:string,
      /**  AP Invoice Number sent to Tax Connect  */  
   APInvoiceNum:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Actions available for tax reconciliation. Delimited by list-delim and sublist-delim  */  
   AvailableActionOptions:string,
      /**  ActionDescription  */  
   ActionDescription:string,
   LastReconActionDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TaxSvcHeadListTableset{
   TaxSvcHeadList:Erp_Tablesets_TaxSvcHeadListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_TaxSvcHeadRow{
      /**  Company Identifier  */  
   Company:string,
      /**  'Type + - (OrderNum, InvoiceNum,  QuoteNum or TCDocID)'. Depending on the type, where Type is O=order, Q = quote, I = invoice, T=tax service doc ID (this is used to create an TaxSvcHead for tax reoconciliation when Tax Connect has a record with no corresponding Epicor record). Example: O-1234 is order type and order number 1234; Q-1234 is quote type and quote number 1234, etc.  */  
   TaxSvcID:string,
      /**  Link to Sales Orders  */  
   OrderNum:number,
      /**  Link to Invoice or Credit Memo  */  
   InvoiceNum:number,
      /**  Document Date  */  
   DocDate:string,
      /**  Customer number  */  
   CustNum:number,
      /**  Doc Code passed to the GetTax function. Can represent an AR Invoice, AP Invoice or Sales Order.  */  
   DocCodes:string,
      /**  Posted / Unposted  */  
   DocState:string,
      /**  Saved / Posted / Committed / Cancelled  */  
   RemoteState:string,
      /**  Sum of taxable amounts  */  
   TotalAmount:number,
      /**  Sum of tax amounts  */  
   TotalTax:number,
      /**  Sum of all line discounts  */  
   TotalDiscount:number,
      /**  Indicates a reconciliation action has been executed by Perform Reconciliation for this TaxSvcHead. The action performed is in LastReconAction  */  
   Reconciled:boolean,
      /**  SalesOrder = 0, SalesInvoice = 1, ReturnInvoice = 5  */  
   DocType:number,
      /**  The unique id assigned by the tax service. Returned by the tax service.  */  
   DocID:number,
      /**  Designates the document currency display symbol for the Epicor invoice Doc currency code  */  
   DocDisplaySymbol:string,
      /**  Link to Quote  */  
   QuoteNum:number,
      /**  The date the TaxSvcHead entry was created  */  
   DateCreated:string,
      /**  The time this entry was created.  */  
   TimeCreated:number,
      /**  DocDate from ReconcileTaxHistory call  */  
   TCHDocCode:string,
      /**   DocStatus from ReconcileTaxHistory call
Requires Code/Desc:
S = Saved
P = Posted
C = Committed
X = Cancelled  */  
   TCHRemoteState:string,
      /**  TotalAmount from ReconcileTaxHistoryCall  */  
   TCHTotalAmount:number,
      /**  TotalDiscount from ReconcileTaxHistory call  */  
   TCHTotalDiscount:number,
      /**  TotalTax from ReconcileTaxHistory call.  */  
   TCHTotalTax:number,
      /**   ResultCode returned by GetTax call.
Code/desc data.  Avalara will return a single code for each address validation request. Success = Operation Succeeded; Warning = Warnings occurred, operation succeeded, Error = Errors occured, operation failed; Exception = Unexpected exceptions occurred, operation failed.  */  
   ResultCode:string,
      /**  DocDate from ReconcileTaxHistory call  */  
   TCHDocDate:string,
      /**   Action to be performed by the Tax Reconciliation Perform Reconcile option. Code/Desc:
N= None, X=Cancel, C=Commit, P=Post, G=GetTax, PC=Post and commit  */  
   Action:string,
      /**   Indicates the last reconciliation action that was performed by Perform Reconcilation for this TaxSvcHead. Needs code/desc:
N= None, X=Cancel, C=Commit, P=Post, G=GetTax, PC=Post and commit  */  
   LastReconAction:string,
      /**  AP Invoice Number sent to Tax Connect  */  
   APInvoiceNum:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Actions available for tax reconciliation. Delimited by list-delim and sublist-delim  */  
   AvailableActionOptions:string,
      /**  ActionDescription  */  
   ActionDescription:string,
   LastReconActionDesc:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TaxSvcJurDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  'Type + - (OrderNum, InvoiceNum,  QuoteNum or TCDocID)'. Depending on the type, where Type is O=order, Q = quote, I = invoice, T=tax service doc ID (this is used to create an TaxSvcHead for tax reoconciliation when Tax Connect has a record with no corresponding Epicor record). Example: O-1234 is order type and order number 1234; Q-1234 is quote type and quote number 1234, etc.  */  
   TaxSvcID:string,
      /**  Invoice, Quote or Order Line number  */  
   LineNum:number,
      /**  For SO, the release number associated with this tax detail, for other types it will be zero.  */  
   OrderRelNum:number,
      /**  Sequence to keep the key unique per TaxSvcID, LineNum, OrderRelNum because there can be multiple jurisdiction tax details for each document/Line/Release combination.  */  
   Seq:number,
      /**  From TaxDetail Base, the taxable amount. In Doc currency.  */  
   TaxableAmount:number,
      /**  Jurisdiction Code for the taxing jurisdiction from GetTax call  */  
   JurisCode:string,
      /**  Jurisdiction name returned by GetTax call.  */  
   JurisName:string,
      /**   Jurisdiction Type from GetTax call describes the jurisdiction for which a particular tax is applied to a document.
This needs Code/desc data  Avalara will return Composite = Unspecified Jurisdiction; State = State, County = County; City = City; Special = Special Tax Jurisdiction.  */  
   JurisType:string,
      /**  The tax rate, i.e. the rate of taxation (0.0 - 1.0). From TaxDetail Rate returned by GetTax call  */  
   Percent:number,
      /**  The tax amount, i.e. the calculated tax. From TaxDetail Tax in GetTax call. In Doc currency.  */  
   TaxAmt:number,
      /**   TaxDetail.Tax type returned by GetTax call
This needs Code/desc data set up: Avalara will return S = Sales Tax; U = Use Tax.  */  
   TaxType:string,
      /**  Same as TaxSvcHead DocID. The unique id assigned by the tax service in GetTax or ReconcileTaxHistory call. Used to match GetTax data with ReconcileTaxHistory data.  */  
   DocID:number,
      /**  The line number that is used by Avalara for this TaxSvcDetail. It will consist of LineNum + OrderRelNum + a generated sequence number to keep the line number unique in Avalara. This is required because we send separate tax Line[] entries to GetTax for the line/release and each of its misc charge codes. In that case all of the line and release numbers are the same for GetTax on the line/release and misc charges, so we append a sequence counter unique to that line/release combination so we can properly sort the tax results.  */  
   TCNo:string,
      /**  From TaxDetail Base, the taxable amount from GetTaxHistory call. In Doc currency.  */  
   TCHTaxableAmount:number,
      /**  Jurisdiction Code for the taxing jurisdiction from GetTaxHistory call  */  
   TCHJurisCode:string,
      /**  Jurisdiction name returned by GetTaxHistory call.  */  
   TCHJurisName:string,
      /**   Jurisdiction Type from GetTaxHistory call.
This needs Code/desc data  Avalara will return Composite = Unspecified Jurisdiction; State = State, County = County; City = City; Special = Special Tax Jurisdiction.  */  
   TCHJurisType:string,
      /**  The tax rate, i.e. the rate of taxation (0.0 - 1.0). From TaxDetail Rate returned by GetTaxHistory call  */  
   TCHPercent:number,
      /**  The tax amount, i.e. the calculated tax. From TaxDetail Tax in GetTaxHistory call. In Doc currency.  */  
   TCHTaxAmt:number,
      /**   TaxDetail.Tax type returned by GetTaxHistory call
This needs Code/desc data set up: Avalara will return S = Sales Tax; U = Use Tax.  */  
   TCHTaxType:string,
      /**  The ItemSeq used when generating the value for the third sector of TaxSvcDetail TCNo.  */  
   ItemSeq:number,
      /**  Quote number is an integer which is used to uniquely identify a quote within the system.  */  
   QuoteNum:number,
      /**  When creating a new order the user is prompted for an order number.  */  
   OrderNum:number,
      /**  Invoice number of the related invoice.  */  
   InvoiceNum:number,
      /**  AP Invoice Number sent to Tax Connect  */  
   APInvoiceNum:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TaxSvcMessagesRow{
      /**  Company Identifier  */  
   Company:string,
      /**  'Type + - (OrderNum or InvoiceNum or QuoteNum'. Depending on the type, where Type is O=order, Q = quote and I = invoice. Example: O-1234 is order type and order number 1234; Q-1234 is quote type and quote number 1234, etc. Used to link TaxSvcMessages to TaxSvcHead  */  
   TaxSvcID:string,
      /**  Sequence of TaxSvcMessage  */  
   Sequence:number,
      /**  Link to Sales Order  */  
   OrderNum:number,
      /**  Link to Invoice  */  
   InvoiceNum:number,
      /**  Line number of item of the invoice or sales order  */  
   LineNum:number,
      /**  Line number of item in remote tax system  */  
   DocLineNum:number,
      /**  Detail of the message  */  
   Detail:string,
      /**  URL of help page for this messag  */  
   HelpLink:string,
      /**  Success, Warning, Error, Exception  */  
   Severity:string,
      /**  Summary of the message  */  
   Summary:string,
      /**  Unique identifier in remote tax system  */  
   DocID:number,
      /**  Name of the message  */  
   Name:string,
      /**  The item the message is referring to  */  
   RefersTo:string,
      /**  Source of the message  */  
   Source:string,
      /**  Link to Quote  */  
   QuoteNum:number,
      /**  For SO, the release number associated with the message.  */  
   OrderRelNum:number,
      /**  AP Invoice Number sent to Tax Connect  */  
   APInvoiceNum:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtTaxResultsTableset{
   TaxSvcHead:Erp_Tablesets_TaxSvcHeadRow[],
   TaxSvcDetail:Erp_Tablesets_TaxSvcDetailRow[],
   TaxSvcJurDtl:Erp_Tablesets_TaxSvcJurDtlRow[],
   TaxSvcMessages:Erp_Tablesets_TaxSvcMessagesRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param taxSvcID
   */  
export interface GetByID_input{
   taxSvcID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_TaxResultsTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_TaxResultsTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_TaxResultsTableset[],
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
   returnObj:Erp_Tablesets_TaxSvcHeadListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param taxSvcID
   */  
export interface GetNewTaxSvcDetail_input{
   ds:Erp_Tablesets_TaxResultsTableset[],
   taxSvcID:string,
}

export interface GetNewTaxSvcDetail_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaxResultsTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewTaxSvcHead_input{
   ds:Erp_Tablesets_TaxResultsTableset[],
}

export interface GetNewTaxSvcHead_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaxResultsTableset[],
}
}

   /** Required : 
      @param ds
      @param taxSvcID
      @param tcNo
   */  
export interface GetNewTaxSvcJurDtl_input{
   ds:Erp_Tablesets_TaxResultsTableset[],
   taxSvcID:string,
   tcNo:string,
}

export interface GetNewTaxSvcJurDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaxResultsTableset[],
}
}

   /** Required : 
      @param ds
      @param taxSvcID
   */  
export interface GetNewTaxSvcMessages_input{
   ds:Erp_Tablesets_TaxResultsTableset[],
   taxSvcID:string,
}

export interface GetNewTaxSvcMessages_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaxResultsTableset[],
}
}

   /** Required : 
      @param whereClauseTaxSvcHead
      @param whereClauseTaxSvcDetail
      @param whereClauseTaxSvcJurDtl
      @param whereClauseTaxSvcMessages
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseTaxSvcHead:string,
   whereClauseTaxSvcDetail:string,
   whereClauseTaxSvcJurDtl:string,
   whereClauseTaxSvcMessages:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_TaxResultsTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param company
      @param apVen
      @param hedNum
   */  
export interface GetTaxSvcID_input{
   company:string,
   apVen:number,
   hedNum:string,
}

export interface GetTaxSvcID_output{
   returnObj:string,
}

   /** Required : 
      @param hedNum
   */  
export interface GetVendorTaxSvcID_input{
   hedNum:string,
}

export interface GetVendorTaxSvcID_output{
   returnObj:string,
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
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtTaxResultsTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtTaxResultsTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_TaxResultsTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaxResultsTableset[],
}
}

