import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PkgControlJobOutputByPCIDSvc
# Description: 
# Version: v1



#########################################################################
# OData methods:
#########################################################################
async def getServiceDocument(epicorHeaders = None):
   """  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => application/json
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlJobOutputByPCIDSvc/",headers=creds) as resp:
           return await resp.json()

async def get_metadata(epicorHeaders = None):
   """  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: Returns metadata document => content
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlJobOutputByPCIDSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PkgControlJobOutputByPCIDs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PkgControlJobOutputByPCIDs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PkgControlJobOutputByPCIDs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PkgControlJobOutputByPCIDRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlJobOutputByPCIDSvc/PkgControlJobOutputByPCIDs",headers=creds) as resp:
           return await resp.json()

async def post_PkgControlJobOutputByPCIDs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PkgControlJobOutputByPCIDs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PkgControlJobOutputByPCIDRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PkgControlJobOutputByPCIDRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlJobOutputByPCIDSvc/PkgControlJobOutputByPCIDs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PkgControlJobOutputByPCIDs_Company_Seq(Company, Seq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PkgControlJobOutputByPCID item
   Description: Calls GetByID to retrieve the PkgControlJobOutputByPCID item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PkgControlJobOutputByPCID
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PkgControlJobOutputByPCIDRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlJobOutputByPCIDSvc/PkgControlJobOutputByPCIDs(" + Company + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PkgControlJobOutputByPCIDs_Company_Seq(Company, Seq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PkgControlJobOutputByPCID for the service
   Description: Calls UpdateExt to update PkgControlJobOutputByPCID. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PkgControlJobOutputByPCID
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PkgControlJobOutputByPCIDRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlJobOutputByPCIDSvc/PkgControlJobOutputByPCIDs(" + Company + "," + Seq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PkgControlJobOutputByPCIDs_Company_Seq(Company, Seq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PkgControlJobOutputByPCID item
   Description: Call UpdateExt to delete PkgControlJobOutputByPCID item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PkgControlJobOutputByPCID
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlJobOutputByPCIDSvc/PkgControlJobOutputByPCIDs(" + Company + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PkgControlJobOutputPartials(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PkgControlJobOutputPartials items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PkgControlJobOutputPartials
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PkgControlJobOutputPartialRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlJobOutputByPCIDSvc/PkgControlJobOutputPartials",headers=creds) as resp:
           return await resp.json()

async def post_PkgControlJobOutputPartials(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PkgControlJobOutputPartials
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PkgControlJobOutputPartialRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PkgControlJobOutputPartialRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlJobOutputByPCIDSvc/PkgControlJobOutputPartials", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PkgControlJobOutputPartials_Company_Seq(Company, Seq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PkgControlJobOutputPartial item
   Description: Calls GetByID to retrieve the PkgControlJobOutputPartial item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PkgControlJobOutputPartial
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PkgControlJobOutputPartialRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlJobOutputByPCIDSvc/PkgControlJobOutputPartials(" + Company + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PkgControlJobOutputPartials_Company_Seq(Company, Seq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PkgControlJobOutputPartial for the service
   Description: Calls UpdateExt to update PkgControlJobOutputPartial. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PkgControlJobOutputPartial
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PkgControlJobOutputPartialRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlJobOutputByPCIDSvc/PkgControlJobOutputPartials(" + Company + "," + Seq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PkgControlJobOutputPartials_Company_Seq(Company, Seq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PkgControlJobOutputPartial item
   Description: Call UpdateExt to delete PkgControlJobOutputPartial item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PkgControlJobOutputPartial
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlJobOutputByPCIDSvc/PkgControlJobOutputPartials(" + Company + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def get_List(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PkgControlJobOutputByPCIDListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlJobOutputByPCIDSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePkgControlJobOutputByPCID, whereClausePkgControlJobOutputPartial, pageSize, absolutePage, epicorHeaders = None):
   """  
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
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePkgControlJobOutputByPCID=" + whereClausePkgControlJobOutputByPCID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePkgControlJobOutputPartial=" + whereClausePkgControlJobOutputPartial
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlJobOutputByPCIDSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(company, seq, epicorHeaders = None):
   """  
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
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "company=" + company
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "seq=" + seq

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlJobOutputByPCIDSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      :param whereClause: Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      :param pageSize: Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      :param absolutePage: Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlJobOutputByPCIDSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_Init(epicorHeaders = None):
   """  
   Summary: Invoke method Init
   OperationID: Init
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Init_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlJobOutputByPCIDSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetJobOperations(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetJobOperations
   Description: Purpose:
Parameters:
<param name="ipEmpID">Employee ID</param><param name="ipIsMES">isMES</param><returns>Erp.BO.PkgControlJobOutputByPCIDTableset</returns>
Notes:
   OperationID: GetJobOperations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetJobOperations_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetJobOperations_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlJobOutputByPCIDSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListStageRecords(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListStageRecords
   OperationID: GetListStageRecords
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListStageRecords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListStageRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlJobOutputByPCIDSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FillPackageCodes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FillPackageCodes
   OperationID: FillPackageCodes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FillPackageCodes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FillPackageCodes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlJobOutputByPCIDSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ReprintLastLabel(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ReprintLastLabel
   OperationID: ReprintLastLabel
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReprintLastLabel_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReprintLastLabel_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlJobOutputByPCIDSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GeneratePCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GeneratePCID
   OperationID: GeneratePCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GeneratePCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GeneratePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlJobOutputByPCIDSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SuppressPrintMessages(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SuppressPrintMessages
   Description: Returns if the employee has the 'Suppress Print Messages' flag on
   OperationID: SuppressPrintMessages
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SuppressPrintMessages_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SuppressPrintMessages_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlJobOutputByPCIDSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsAutoPrintSetup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsAutoPrintSetup
   Description: To verify if autoprint is setup
   OperationID: IsAutoPrintSetup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsAutoPrintSetup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsAutoPrintSetup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlJobOutputByPCIDSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowID(id, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "id=" + id

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlJobOutputByPCIDSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowIDs(ids, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ids=" + ids

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlJobOutputByPCIDSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_Update(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlJobOutputByPCIDSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlJobOutputByPCIDSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlJobOutputByPCIDListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PkgControlJobOutputByPCIDListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlJobOutputByPCIDRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PkgControlJobOutputByPCIDRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlJobOutputPartialRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PkgControlJobOutputPartialRow] = obj["value"]
      pass

class Erp_Tablesets_PkgControlJobOutputByPCIDListRow:
   def __init__(self, obj):
      self.Asm:int = obj["Asm"]
      self.Company:str = obj["Company"]
      self.EmpID:str = obj["EmpID"]
      self.EmpName:str = obj["EmpName"]
      self.EmpQtyCompl:int = obj["EmpQtyCompl"]
      self.Job:str = obj["Job"]
      self.OprSeq:int = obj["OprSeq"]
      self.Part:str = obj["Part"]
      self.PartDesc:str = obj["PartDesc"]
      self.PkgCode:str = obj["PkgCode"]
      self.PkgCodeDesc:str = obj["PkgCodeDesc"]
      self.PkgCodeQty:int = obj["PkgCodeQty"]
      self.PkgDisplayHidden:bool = obj["PkgDisplayHidden"]
      self.Printer:str = obj["Printer"]
      self.QtyCompleted:int = obj["QtyCompleted"]
      self.Select:bool = obj["Select"]
      self.Seq:int = obj["Seq"]
      self.Shift:int = obj["Shift"]
      self.UOM:str = obj["UOM"]
      self.PCID:str = obj["PCID"]
      self.IsMES:bool = obj["IsMES"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PkgControlJobOutputByPCIDRow:
   def __init__(self, obj):
      self.Asm:int = obj["Asm"]
      self.Company:str = obj["Company"]
      self.EmpQtyCompl:int = obj["EmpQtyCompl"]
      self.Job:str = obj["Job"]
      self.Part:str = obj["Part"]
      self.PartDesc:str = obj["PartDesc"]
      self.PkgCode:str = obj["PkgCode"]
      self.PkgCodeDesc:str = obj["PkgCodeDesc"]
      self.PkgCodeQty:int = obj["PkgCodeQty"]
      self.Printer:str = obj["Printer"]
      self.QtyCompleted:int = obj["QtyCompleted"]
      self.Select:bool = obj["Select"]
      self.Seq:int = obj["Seq"]
      self.UOM:str = obj["UOM"]
      self.EmpName:str = obj["EmpName"]
      self.OprSeq:int = obj["OprSeq"]
      self.Shift:int = obj["Shift"]
      self.PkgDisplayHidden:bool = obj["PkgDisplayHidden"]
      self.EmpID:str = obj["EmpID"]
      self.PCID:str = obj["PCID"]
      self.IsMES:bool = obj["IsMES"]
      self.ReportStyle:int = obj["ReportStyle"]
      """  Report Style usually taken from the label type  """  
      self.NumLabelsToPrint:int = obj["NumLabelsToPrint"]
      """  Quantity of labels to be printed, usually taken from the label type  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PkgControlJobOutputPartialRow:
   def __init__(self, obj):
      self.Asm:int = obj["Asm"]
      self.Company:str = obj["Company"]
      self.EmpID:str = obj["EmpID"]
      self.EmpQtyCompl:int = obj["EmpQtyCompl"]
      self.Job:str = obj["Job"]
      self.OprSeq:int = obj["OprSeq"]
      self.Part:str = obj["Part"]
      self.PartDesc:str = obj["PartDesc"]
      self.PCID:str = obj["PCID"]
      self.PkgCode:str = obj["PkgCode"]
      self.PkgCodeDesc:str = obj["PkgCodeDesc"]
      self.PkgCodeQty:int = obj["PkgCodeQty"]
      self.PkgDisplayHidden:bool = obj["PkgDisplayHidden"]
      self.Printer:str = obj["Printer"]
      self.QtyCompleted:int = obj["QtyCompleted"]
      self.Select:bool = obj["Select"]
      self.Seq:int = obj["Seq"]
      self.Shift:int = obj["Shift"]
      self.UOM:str = obj["UOM"]
      self.EmpName:str = obj["EmpName"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_PkgControlJobOutputByPCIDListRow:
   def __init__(self, obj):
      self.Asm:int = obj["Asm"]
      self.Company:str = obj["Company"]
      self.EmpID:str = obj["EmpID"]
      self.EmpName:str = obj["EmpName"]
      self.EmpQtyCompl:int = obj["EmpQtyCompl"]
      self.Job:str = obj["Job"]
      self.OprSeq:int = obj["OprSeq"]
      self.Part:str = obj["Part"]
      self.PartDesc:str = obj["PartDesc"]
      self.PkgCode:str = obj["PkgCode"]
      self.PkgCodeDesc:str = obj["PkgCodeDesc"]
      self.PkgCodeQty:int = obj["PkgCodeQty"]
      self.PkgDisplayHidden:bool = obj["PkgDisplayHidden"]
      self.Printer:str = obj["Printer"]
      self.QtyCompleted:int = obj["QtyCompleted"]
      self.Select:bool = obj["Select"]
      self.Seq:int = obj["Seq"]
      self.Shift:int = obj["Shift"]
      self.UOM:str = obj["UOM"]
      self.PCID:str = obj["PCID"]
      self.IsMES:bool = obj["IsMES"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PkgControlJobOutputByPCIDListTableset:
   def __init__(self, obj):
      self.PkgControlJobOutputByPCIDList:list[Erp_Tablesets_PkgControlJobOutputByPCIDListRow] = obj["PkgControlJobOutputByPCIDList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PkgControlJobOutputByPCIDRow:
   def __init__(self, obj):
      self.Asm:int = obj["Asm"]
      self.Company:str = obj["Company"]
      self.EmpQtyCompl:int = obj["EmpQtyCompl"]
      self.Job:str = obj["Job"]
      self.Part:str = obj["Part"]
      self.PartDesc:str = obj["PartDesc"]
      self.PkgCode:str = obj["PkgCode"]
      self.PkgCodeDesc:str = obj["PkgCodeDesc"]
      self.PkgCodeQty:int = obj["PkgCodeQty"]
      self.Printer:str = obj["Printer"]
      self.QtyCompleted:int = obj["QtyCompleted"]
      self.Select:bool = obj["Select"]
      self.Seq:int = obj["Seq"]
      self.UOM:str = obj["UOM"]
      self.EmpName:str = obj["EmpName"]
      self.OprSeq:int = obj["OprSeq"]
      self.Shift:int = obj["Shift"]
      self.PkgDisplayHidden:bool = obj["PkgDisplayHidden"]
      self.EmpID:str = obj["EmpID"]
      self.PCID:str = obj["PCID"]
      self.IsMES:bool = obj["IsMES"]
      self.ReportStyle:int = obj["ReportStyle"]
      """  Report Style usually taken from the label type  """  
      self.NumLabelsToPrint:int = obj["NumLabelsToPrint"]
      """  Quantity of labels to be printed, usually taken from the label type  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PkgControlJobOutputByPCIDTableset:
   def __init__(self, obj):
      self.PkgControlJobOutputByPCID:list[Erp_Tablesets_PkgControlJobOutputByPCIDRow] = obj["PkgControlJobOutputByPCID"]
      self.PkgControlJobOutputPartial:list[Erp_Tablesets_PkgControlJobOutputPartialRow] = obj["PkgControlJobOutputPartial"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PkgControlJobOutputPartialRow:
   def __init__(self, obj):
      self.Asm:int = obj["Asm"]
      self.Company:str = obj["Company"]
      self.EmpID:str = obj["EmpID"]
      self.EmpQtyCompl:int = obj["EmpQtyCompl"]
      self.Job:str = obj["Job"]
      self.OprSeq:int = obj["OprSeq"]
      self.Part:str = obj["Part"]
      self.PartDesc:str = obj["PartDesc"]
      self.PCID:str = obj["PCID"]
      self.PkgCode:str = obj["PkgCode"]
      self.PkgCodeDesc:str = obj["PkgCodeDesc"]
      self.PkgCodeQty:int = obj["PkgCodeQty"]
      self.PkgDisplayHidden:bool = obj["PkgDisplayHidden"]
      self.Printer:str = obj["Printer"]
      self.QtyCompleted:int = obj["QtyCompleted"]
      self.Select:bool = obj["Select"]
      self.Seq:int = obj["Seq"]
      self.Shift:int = obj["Shift"]
      self.UOM:str = obj["UOM"]
      self.EmpName:str = obj["EmpName"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtPkgControlJobOutputByPCIDTableset:
   def __init__(self, obj):
      self.PkgControlJobOutputByPCID:list[Erp_Tablesets_PkgControlJobOutputByPCIDRow] = obj["PkgControlJobOutputByPCID"]
      self.PkgControlJobOutputPartial:list[Erp_Tablesets_PkgControlJobOutputPartialRow] = obj["PkgControlJobOutputPartial"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class FillPackageCodes_input:
   """ Required : 
   seq
   ds
   """  
   def __init__(self, obj):
      self.seq:int = obj["seq"]
      """  unique sequence  """  
      self.ds:list[Erp_Tablesets_PkgControlJobOutputByPCIDTableset] = obj["ds"]
      pass

class FillPackageCodes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlJobOutputByPCIDTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GeneratePCID_input:
   """ Required : 
   seq
   ds
   """  
   def __init__(self, obj):
      self.seq:int = obj["seq"]
      """  unique sequence  """  
      self.ds:list[Erp_Tablesets_PkgControlJobOutputByPCIDTableset] = obj["ds"]
      pass

class GeneratePCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlJobOutputByPCIDTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   company
   seq
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.seq:int = obj["seq"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PkgControlJobOutputByPCIDTableset] = obj["returnObj"]
      pass

class GetBySysRowID_input:
   """ Required : 
   id
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      pass

class GetBySysRowID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PkgControlJobOutputByPCIDTableset] = obj["returnObj"]
      pass

class GetBySysRowIDs_input:
   """ Required : 
   ids
   """  
   def __init__(self, obj):
      self.ids:str = obj["ids"]
      pass

class GetBySysRowIDs_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PkgControlJobOutputByPCIDTableset] = obj["returnObj"]
      pass

class GetJobOperations_input:
   """ Required : 
   ipEmpID
   ipIsMES
   """  
   def __init__(self, obj):
      self.ipEmpID:str = obj["ipEmpID"]
      self.ipIsMES:bool = obj["ipIsMES"]
      pass

class GetJobOperations_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PkgControlJobOutputByPCIDTableset] = obj["returnObj"]
      pass

class GetListStageRecords_input:
   """ Required : 
   ds
   ipEmpID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlJobOutputByPCIDTableset] = obj["ds"]
      self.ipEmpID:str = obj["ipEmpID"]
      """  ipEmpID  """  
      pass

class GetListStageRecords_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlJobOutputByPCIDTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PkgControlJobOutputByPCIDListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePkgControlJobOutputByPCID
   whereClausePkgControlJobOutputPartial
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePkgControlJobOutputByPCID:str = obj["whereClausePkgControlJobOutputByPCID"]
      self.whereClausePkgControlJobOutputPartial:str = obj["whereClausePkgControlJobOutputPartial"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PkgControlJobOutputByPCIDTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class Ice_BOUpdErrorRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.ErrorLevel:str = obj["ErrorLevel"]
      self.ErrorType:str = obj["ErrorType"]
      self.ErrorText:str = obj["ErrorText"]
      self.ErrorSysRowID:str = obj["ErrorSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_BOUpdErrorTableset:
   def __init__(self, obj):
      self.BOUpdError:list[Ice_BOUpdErrorRow] = obj["BOUpdError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Extensions_ExtensionRow:
   def __init__(self, obj):
      self.ColumnValues:object
      self.RowMod:str = obj["RowMod"]
      self.SysRowID:str = obj["SysRowID"]
      pass

class Ice_Extensions_ExtensionTableColumn:
   def __init__(self, obj):
      self.ColumnName:str = obj["ColumnName"]
      self.ColumnType:str = obj["ColumnType"]
      pass

class Ice_Extensions_ExtensionTableData:
   def __init__(self, obj):
      self.Table:list[Ice_Extensions_ExtensionRow] = obj["Table"]
      self.SystemCode:str = obj["SystemCode"]
      self.TableName:str = obj["TableName"]
      self.Columns:list[Ice_Extensions_ExtensionTableColumn] = obj["Columns"]
      self.PrimaryKeyColumns:str = obj["PrimaryKeyColumns"]
      self.PeerTableSystemCode:str = obj["PeerTableSystemCode"]
      self.PeerTableName:str = obj["PeerTableName"]
      pass

class Init_output:
   def __init__(self, obj):
      pass

class IsAutoPrintSetup_input:
   """ Required : 
   ipWriteToStaged
   """  
   def __init__(self, obj):
      self.ipWriteToStaged:bool = obj["ipWriteToStaged"]
      """  write to staged table  """  
      pass

class IsAutoPrintSetup_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ReprintLastLabel_input:
   """ Required : 
   ipSeq
   ds
   """  
   def __init__(self, obj):
      self.ipSeq:int = obj["ipSeq"]
      """  unique sequence  """  
      self.ds:list[Erp_Tablesets_PkgControlJobOutputByPCIDTableset] = obj["ds"]
      pass

class ReprintLastLabel_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlJobOutputByPCIDTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SuppressPrintMessages_input:
   """ Required : 
   empID
   """  
   def __init__(self, obj):
      self.empID:str = obj["empID"]
      """  Employee ID  """  
      pass

class SuppressPrintMessages_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  True if messages should be hidden  """  
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPkgControlJobOutputByPCIDTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPkgControlJobOutputByPCIDTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlJobOutputByPCIDTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlJobOutputByPCIDTableset] = obj["ds"]
      pass

      """  output parameters  """  

