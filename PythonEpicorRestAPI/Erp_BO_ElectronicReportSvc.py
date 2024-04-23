import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ElectronicReportSvc
# Description: ElectronicReportSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicReportSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicReportSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ElectronicReports(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ElectronicReports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ElectronicReports
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ElectronicReportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicReportSvc/ElectronicReports",headers=creds) as resp:
           return await resp.json()

async def post_ElectronicReports(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ElectronicReports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ElectronicReportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ElectronicReportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicReportSvc/ElectronicReports", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ElectronicReports_Company_EFTHeadUID(Company, EFTHeadUID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ElectronicReport item
   Description: Calls GetByID to retrieve the ElectronicReport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ElectronicReport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EFTHeadUID: Desc: EFTHeadUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ElectronicReportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicReportSvc/ElectronicReports(" + Company + "," + EFTHeadUID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ElectronicReports_Company_EFTHeadUID(Company, EFTHeadUID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ElectronicReport for the service
   Description: Calls UpdateExt to update ElectronicReport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ElectronicReport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EFTHeadUID: Desc: EFTHeadUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ElectronicReportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicReportSvc/ElectronicReports(" + Company + "," + EFTHeadUID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ElectronicReports_Company_EFTHeadUID(Company, EFTHeadUID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ElectronicReport item
   Description: Call UpdateExt to delete ElectronicReport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ElectronicReport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EFTHeadUID: Desc: EFTHeadUID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicReportSvc/ElectronicReports(" + Company + "," + EFTHeadUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ElectronicReports_Company_EFTHeadUID_ElectronicReportProps(Company, EFTHeadUID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ElectronicReportProps items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ElectronicReportProps1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EFTHeadUID: Desc: EFTHeadUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ElectronicReportPropRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicReportSvc/ElectronicReports(" + Company + "," + EFTHeadUID + ")/ElectronicReportProps",headers=creds) as resp:
           return await resp.json()

async def get_ElectronicReports_Company_EFTHeadUID_ElectronicReportProps_Company_EFTHeadUID_EFTPropUID(Company, EFTHeadUID, EFTPropUID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ElectronicReportProp item
   Description: Calls GetByID to retrieve the ElectronicReportProp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ElectronicReportProp1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EFTHeadUID: Desc: EFTHeadUID   Required: True
      :param EFTPropUID: Desc: EFTPropUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ElectronicReportPropRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicReportSvc/ElectronicReports(" + Company + "," + EFTHeadUID + ")/ElectronicReportProps(" + Company + "," + EFTHeadUID + "," + EFTPropUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ElectronicReportProps(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ElectronicReportProps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ElectronicReportProps
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ElectronicReportPropRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicReportSvc/ElectronicReportProps",headers=creds) as resp:
           return await resp.json()

async def post_ElectronicReportProps(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ElectronicReportProps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ElectronicReportPropRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ElectronicReportPropRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicReportSvc/ElectronicReportProps", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ElectronicReportProps_Company_EFTHeadUID_EFTPropUID(Company, EFTHeadUID, EFTPropUID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ElectronicReportProp item
   Description: Calls GetByID to retrieve the ElectronicReportProp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ElectronicReportProp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EFTHeadUID: Desc: EFTHeadUID   Required: True
      :param EFTPropUID: Desc: EFTPropUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ElectronicReportPropRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicReportSvc/ElectronicReportProps(" + Company + "," + EFTHeadUID + "," + EFTPropUID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ElectronicReportProps_Company_EFTHeadUID_EFTPropUID(Company, EFTHeadUID, EFTPropUID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ElectronicReportProp for the service
   Description: Calls UpdateExt to update ElectronicReportProp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ElectronicReportProp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EFTHeadUID: Desc: EFTHeadUID   Required: True
      :param EFTPropUID: Desc: EFTPropUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ElectronicReportPropRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicReportSvc/ElectronicReportProps(" + Company + "," + EFTHeadUID + "," + EFTPropUID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ElectronicReportProps_Company_EFTHeadUID_EFTPropUID(Company, EFTHeadUID, EFTPropUID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ElectronicReportProp item
   Description: Call UpdateExt to delete ElectronicReportProp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ElectronicReportProp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EFTHeadUID: Desc: EFTHeadUID   Required: True
      :param EFTPropUID: Desc: EFTPropUID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicReportSvc/ElectronicReportProps(" + Company + "," + EFTHeadUID + "," + EFTPropUID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ElectronicReportListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicReportSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseElectronicReport, whereClauseElectronicReportProp, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseElectronicReport=" + whereClauseElectronicReport
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseElectronicReportProp=" + whereClauseElectronicReportProp
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicReportSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(efTHeadUID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "efTHeadUID=" + efTHeadUID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicReportSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicReportSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GenerateEUSalesReport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateEUSalesReport
   Description: GenerateTaxTranReport.
   OperationID: GenerateEUSalesReport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateEUSalesReport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateEUSalesReport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateTaxBoxReport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateTaxBoxReport
   Description: GenerateTaxBoxReport.
   OperationID: GenerateTaxBoxReport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateTaxBoxReport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateTaxBoxReport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateTaxTranReport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateTaxTranReport
   Description: GenerateTaxTranReport.
   OperationID: GenerateTaxTranReport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateTaxTranReport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateTaxTranReport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeEFTHeadUID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeEFTHeadUID
   Description: Call this method when the user changes the Electronic Interface.
   OperationID: OnChangeEFTHeadUID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeEFTHeadUID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeEFTHeadUID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewElectronicReport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewElectronicReport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewElectronicReport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewElectronicReport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewElectronicReport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewElectronicReportProp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewElectronicReportProp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewElectronicReportProp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewElectronicReportProp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewElectronicReportProp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicReportSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicReportSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicReportSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicReportSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ElectronicReportListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ElectronicReportListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ElectronicReportPropRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ElectronicReportPropRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ElectronicReportRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ElectronicReportRow] = obj["value"]
      pass

class Erp_Tablesets_ElectronicReportListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  Unique identifier of the EFT. Related to EFTHead.EFTHeadUID.  """  
      self.OutputFile:str = obj["OutputFile"]
      """  This will be the default filename for the output file created by the electronic interface  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ElecReportName:str = obj["ElecReportName"]
      """  Short name of the interface, it should be unique  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ElectronicReportPropRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  Unique identifier of the EFT. Related to EFTHead.EFTHeadUID.  """  
      self.EFTPropUID:int = obj["EFTPropUID"]
      """  Unique identifier of the EFT property. Related to EFTProp.EFTPropUID.  """  
      self.PropValue:str = obj["PropValue"]
      """  Property Value, always defined as string value  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DateCol:str = obj["DateCol"]
      """  Date Column  """  
      self.DecimalCol:int = obj["DecimalCol"]
      """  Decimal Column  """  
      self.ListCol:str = obj["ListCol"]
      """  List Column  """  
      self.LogicalCol:bool = obj["LogicalCol"]
      """  Logical Column  """  
      self.StringCol:str = obj["StringCol"]
      """  String Column  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PropNameType:str = obj["PropNameType"]
      self.PropNameName:str = obj["PropNameName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ElectronicReportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  Unique identifier of the EFT. Related to EFTHead.EFTHeadUID.  """  
      self.OutputFile:str = obj["OutputFile"]
      """  This will be the default filename for the output file created by the electronic interface  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IntrastatDispatchFileName:str = obj["IntrastatDispatchFileName"]
      """  IntrastatDispatchFileName  """  
      self.OutputFileDisplay:str = obj["OutputFileDisplay"]
      self.BitFlag:int = obj["BitFlag"]
      self.ElecReportType:int = obj["ElecReportType"]
      self.ElecReportName:str = obj["ElecReportName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   efTHeadUID
   """  
   def __init__(self, obj):
      self.efTHeadUID:int = obj["efTHeadUID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_ElectronicReportListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  Unique identifier of the EFT. Related to EFTHead.EFTHeadUID.  """  
      self.OutputFile:str = obj["OutputFile"]
      """  This will be the default filename for the output file created by the electronic interface  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ElecReportName:str = obj["ElecReportName"]
      """  Short name of the interface, it should be unique  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ElectronicReportListTableset:
   def __init__(self, obj):
      self.ElectronicReportList:list[Erp_Tablesets_ElectronicReportListRow] = obj["ElectronicReportList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ElectronicReportPropRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  Unique identifier of the EFT. Related to EFTHead.EFTHeadUID.  """  
      self.EFTPropUID:int = obj["EFTPropUID"]
      """  Unique identifier of the EFT property. Related to EFTProp.EFTPropUID.  """  
      self.PropValue:str = obj["PropValue"]
      """  Property Value, always defined as string value  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DateCol:str = obj["DateCol"]
      """  Date Column  """  
      self.DecimalCol:int = obj["DecimalCol"]
      """  Decimal Column  """  
      self.ListCol:str = obj["ListCol"]
      """  List Column  """  
      self.LogicalCol:bool = obj["LogicalCol"]
      """  Logical Column  """  
      self.StringCol:str = obj["StringCol"]
      """  String Column  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PropNameType:str = obj["PropNameType"]
      self.PropNameName:str = obj["PropNameName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ElectronicReportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  Unique identifier of the EFT. Related to EFTHead.EFTHeadUID.  """  
      self.OutputFile:str = obj["OutputFile"]
      """  This will be the default filename for the output file created by the electronic interface  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IntrastatDispatchFileName:str = obj["IntrastatDispatchFileName"]
      """  IntrastatDispatchFileName  """  
      self.OutputFileDisplay:str = obj["OutputFileDisplay"]
      self.BitFlag:int = obj["BitFlag"]
      self.ElecReportType:int = obj["ElecReportType"]
      self.ElecReportName:str = obj["ElecReportName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ElectronicReportTableset:
   def __init__(self, obj):
      self.ElectronicReport:list[Erp_Tablesets_ElectronicReportRow] = obj["ElectronicReport"]
      self.ElectronicReportProp:list[Erp_Tablesets_ElectronicReportPropRow] = obj["ElectronicReportProp"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtElectronicReportTableset:
   def __init__(self, obj):
      self.ElectronicReport:list[Erp_Tablesets_ElectronicReportRow] = obj["ElectronicReport"]
      self.ElectronicReportProp:list[Erp_Tablesets_ElectronicReportPropRow] = obj["ElectronicReportProp"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GenerateEUSalesReport_input:
   """ Required : 
   lRound
   reportIDList
   taxCodeList
   rangeOption
   startDate
   endDate
   eftHeadUID
   """  
   def __init__(self, obj):
      self.lRound:bool = obj["lRound"]
      """  If yes then amounts are rounded  """  
      self.reportIDList:str = obj["reportIDList"]
      """  List of the Tax Report IDs  """  
      self.taxCodeList:str = obj["taxCodeList"]
      """  List of the Tax Codes  """  
      self.rangeOption:str = obj["rangeOption"]
      """  Date Range or VAT Report  """  
      self.startDate:str = obj["startDate"]
      """  Start Date  """  
      self.endDate:str = obj["endDate"]
      """  End Date  """  
      self.eftHeadUID:int = obj["eftHeadUID"]
      """  Electronic Interface unique ID  """  
      pass

class GenerateEUSalesReport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.success:bool = obj["success"]
      pass

      """  output parameters  """  

class GenerateTaxBoxReport_input:
   """ Required : 
   reportID
   eftHeadUID
   """  
   def __init__(self, obj):
      self.reportID:str = obj["reportID"]
      """  VAT Tax Report ID for which export is generated  """  
      self.eftHeadUID:int = obj["eftHeadUID"]
      """  Electronic Interface unique ID  """  
      pass

class GenerateTaxBoxReport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.success:bool = obj["success"]
      pass

      """  output parameters  """  

class GenerateTaxTranReport_input:
   """ Required : 
   reportID
   eftHeadUID
   backdatedItem
   """  
   def __init__(self, obj):
      self.reportID:str = obj["reportID"]
      """  Tax Report ID  """  
      self.eftHeadUID:int = obj["eftHeadUID"]
      """  Electronic Interface unique ID  """  
      self.backdatedItem:int = obj["backdatedItem"]
      """  Backdated Item  """  
      pass

class GenerateTaxTranReport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.success:bool = obj["success"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   efTHeadUID
   """  
   def __init__(self, obj):
      self.efTHeadUID:int = obj["efTHeadUID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ElectronicReportTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ElectronicReportTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ElectronicReportTableset] = obj["returnObj"]
      pass

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
      self.returnObj:list[Erp_Tablesets_ElectronicReportListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewElectronicReportProp_input:
   """ Required : 
   ds
   efTHeadUID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ElectronicReportTableset] = obj["ds"]
      self.efTHeadUID:int = obj["efTHeadUID"]
      pass

class GetNewElectronicReportProp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ElectronicReportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewElectronicReport_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ElectronicReportTableset] = obj["ds"]
      pass

class GetNewElectronicReport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ElectronicReportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseElectronicReport
   whereClauseElectronicReportProp
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseElectronicReport:str = obj["whereClauseElectronicReport"]
      self.whereClauseElectronicReportProp:str = obj["whereClauseElectronicReportProp"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ElectronicReportTableset] = obj["returnObj"]
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

class OnChangeEFTHeadUID_input:
   """ Required : 
   pcEFTHeadUID
   ds
   """  
   def __init__(self, obj):
      self.pcEFTHeadUID:int = obj["pcEFTHeadUID"]
      """  The proposed value of EFTHeadUID.  """  
      self.ds:list[Erp_Tablesets_ElectronicReportTableset] = obj["ds"]
      pass

class OnChangeEFTHeadUID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ElectronicReportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtElectronicReportTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtElectronicReportTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ElectronicReportTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ElectronicReportTableset] = obj["ds"]
      pass

      """  output parameters  """  

