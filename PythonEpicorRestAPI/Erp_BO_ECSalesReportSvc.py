import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ECSalesReportSvc
# Description: Add your summary for this object here
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECSalesReportSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECSalesReportSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ECSalesReports(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ECSalesReports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECSalesReports
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECSalesReportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECSalesReportSvc/ECSalesReports",headers=creds) as resp:
           return await resp.json()

async def post_ECSalesReports(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECSalesReports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECSalesReportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECSalesReportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ECSalesReportSvc/ECSalesReports", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ECSalesReports_Company_ECSalesReportID(Company, ECSalesReportID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECSalesReport item
   Description: Calls GetByID to retrieve the ECSalesReport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECSalesReport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ECSalesReportID: Desc: ECSalesReportID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECSalesReportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECSalesReportSvc/ECSalesReports(" + Company + "," + ECSalesReportID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ECSalesReports_Company_ECSalesReportID(Company, ECSalesReportID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ECSalesReport for the service
   Description: Calls UpdateExt to update ECSalesReport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECSalesReport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ECSalesReportID: Desc: ECSalesReportID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECSalesReportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ECSalesReportSvc/ECSalesReports(" + Company + "," + ECSalesReportID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ECSalesReports_Company_ECSalesReportID(Company, ECSalesReportID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ECSalesReport item
   Description: Call UpdateExt to delete ECSalesReport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECSalesReport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ECSalesReportID: Desc: ECSalesReportID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ECSalesReportSvc/ECSalesReports(" + Company + "," + ECSalesReportID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ECSalesReports_Company_ECSalesReportID_ECSLXMLHeds(Company, ECSalesReportID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ECSLXMLHeds items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ECSLXMLHeds1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ECSalesReportID: Desc: ECSalesReportID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECSLXMLHedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECSalesReportSvc/ECSalesReports(" + Company + "," + ECSalesReportID + ")/ECSLXMLHeds",headers=creds) as resp:
           return await resp.json()

async def get_ECSalesReports_Company_ECSalesReportID_ECSLXMLHeds_Company_ECSalesReportID_HedNum(Company, ECSalesReportID, HedNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECSLXMLHed item
   Description: Calls GetByID to retrieve the ECSLXMLHed item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECSLXMLHed1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ECSalesReportID: Desc: ECSalesReportID   Required: True   Allow empty value : True
      :param HedNum: Desc: HedNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECSLXMLHedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECSalesReportSvc/ECSalesReports(" + Company + "," + ECSalesReportID + ")/ECSLXMLHeds(" + Company + "," + ECSalesReportID + "," + HedNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_ECSLXMLHeds(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ECSLXMLHeds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECSLXMLHeds
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECSLXMLHedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECSalesReportSvc/ECSLXMLHeds",headers=creds) as resp:
           return await resp.json()

async def post_ECSLXMLHeds(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECSLXMLHeds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECSLXMLHedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECSLXMLHedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ECSalesReportSvc/ECSLXMLHeds", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ECSLXMLHeds_Company_ECSalesReportID_HedNum(Company, ECSalesReportID, HedNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECSLXMLHed item
   Description: Calls GetByID to retrieve the ECSLXMLHed item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECSLXMLHed
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ECSalesReportID: Desc: ECSalesReportID   Required: True   Allow empty value : True
      :param HedNum: Desc: HedNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECSLXMLHedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECSalesReportSvc/ECSLXMLHeds(" + Company + "," + ECSalesReportID + "," + HedNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ECSLXMLHeds_Company_ECSalesReportID_HedNum(Company, ECSalesReportID, HedNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ECSLXMLHed for the service
   Description: Calls UpdateExt to update ECSLXMLHed. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECSLXMLHed
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ECSalesReportID: Desc: ECSalesReportID   Required: True   Allow empty value : True
      :param HedNum: Desc: HedNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECSLXMLHedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ECSalesReportSvc/ECSLXMLHeds(" + Company + "," + ECSalesReportID + "," + HedNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ECSLXMLHeds_Company_ECSalesReportID_HedNum(Company, ECSalesReportID, HedNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ECSLXMLHed item
   Description: Call UpdateExt to delete ECSLXMLHed item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECSLXMLHed
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ECSalesReportID: Desc: ECSalesReportID   Required: True   Allow empty value : True
      :param HedNum: Desc: HedNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ECSalesReportSvc/ECSLXMLHeds(" + Company + "," + ECSalesReportID + "," + HedNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_ECSLXMLHeds_Company_ECSalesReportID_HedNum_ECSLXMLDtls(Company, ECSalesReportID, HedNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ECSLXMLDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ECSLXMLDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ECSalesReportID: Desc: ECSalesReportID   Required: True   Allow empty value : True
      :param HedNum: Desc: HedNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECSLXMLDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECSalesReportSvc/ECSLXMLHeds(" + Company + "," + ECSalesReportID + "," + HedNum + ")/ECSLXMLDtls",headers=creds) as resp:
           return await resp.json()

async def get_ECSLXMLHeds_Company_ECSalesReportID_HedNum_ECSLXMLDtls_Company_ECSalesReportID_HedNum_LineNum(Company, ECSalesReportID, HedNum, LineNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECSLXMLDtl item
   Description: Calls GetByID to retrieve the ECSLXMLDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECSLXMLDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ECSalesReportID: Desc: ECSalesReportID   Required: True   Allow empty value : True
      :param HedNum: Desc: HedNum   Required: True
      :param LineNum: Desc: LineNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECSLXMLDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECSalesReportSvc/ECSLXMLHeds(" + Company + "," + ECSalesReportID + "," + HedNum + ")/ECSLXMLDtls(" + Company + "," + ECSalesReportID + "," + HedNum + "," + LineNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_ECSLXMLDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ECSLXMLDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECSLXMLDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECSLXMLDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECSalesReportSvc/ECSLXMLDtls",headers=creds) as resp:
           return await resp.json()

async def post_ECSLXMLDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECSLXMLDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECSLXMLDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECSLXMLDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ECSalesReportSvc/ECSLXMLDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ECSLXMLDtls_Company_ECSalesReportID_HedNum_LineNum(Company, ECSalesReportID, HedNum, LineNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECSLXMLDtl item
   Description: Calls GetByID to retrieve the ECSLXMLDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECSLXMLDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ECSalesReportID: Desc: ECSalesReportID   Required: True   Allow empty value : True
      :param HedNum: Desc: HedNum   Required: True
      :param LineNum: Desc: LineNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECSLXMLDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECSalesReportSvc/ECSLXMLDtls(" + Company + "," + ECSalesReportID + "," + HedNum + "," + LineNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ECSLXMLDtls_Company_ECSalesReportID_HedNum_LineNum(Company, ECSalesReportID, HedNum, LineNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ECSLXMLDtl for the service
   Description: Calls UpdateExt to update ECSLXMLDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECSLXMLDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ECSalesReportID: Desc: ECSalesReportID   Required: True   Allow empty value : True
      :param HedNum: Desc: HedNum   Required: True
      :param LineNum: Desc: LineNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECSLXMLDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ECSalesReportSvc/ECSLXMLDtls(" + Company + "," + ECSalesReportID + "," + HedNum + "," + LineNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ECSLXMLDtls_Company_ECSalesReportID_HedNum_LineNum(Company, ECSalesReportID, HedNum, LineNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ECSLXMLDtl item
   Description: Call UpdateExt to delete ECSLXMLDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECSLXMLDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ECSalesReportID: Desc: ECSalesReportID   Required: True   Allow empty value : True
      :param HedNum: Desc: HedNum   Required: True
      :param LineNum: Desc: LineNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ECSalesReportSvc/ECSLXMLDtls(" + Company + "," + ECSalesReportID + "," + HedNum + "," + LineNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECSalesReportListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECSalesReportSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseECSalesReport, whereClauseECSLXMLHed, whereClauseECSLXMLDtl, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
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
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseECSalesReport=" + whereClauseECSalesReport
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseECSLXMLHed=" + whereClauseECSLXMLHed
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseECSLXMLDtl=" + whereClauseECSLXMLDtl
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECSalesReportSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(ecSalesReportID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
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
   params += "ecSalesReportID=" + ecSalesReportID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECSalesReportSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECSalesReportSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ValidateEMail(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateEMail
   Description: Validation email
   OperationID: ValidateEMail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateEMail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateEMail_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ECSalesReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidatePhone(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidatePhone
   Description: Validation phone number
   OperationID: ValidatePhone
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePhone_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePhone_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ECSalesReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExportData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportData
   Description: Export EU Sales List.
   OperationID: ExportData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ECSalesReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateXMLData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateXMLData
   Description: Generate XML DATA on XML Tables.
   OperationID: GenerateXMLData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateXMLData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateXMLData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ECSalesReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateECSLXMLDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateECSLXMLDtl
   Description: Validate ECSLXMLDtl
   OperationID: ValidateECSLXMLDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateECSLXMLDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateECSLXMLDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ECSalesReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewECSalesReport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewECSalesReport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECSalesReport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECSalesReport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECSalesReport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ECSalesReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewECSLXMLHed(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewECSLXMLHed
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECSLXMLHed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECSLXMLHed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECSLXMLHed_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ECSalesReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewECSLXMLDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewECSLXMLDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECSLXMLDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECSLXMLDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECSLXMLDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ECSalesReportSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ECSalesReportSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECSalesReportSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECSalesReportSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ECSalesReportSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ECSalesReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECSLXMLDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ECSLXMLDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECSLXMLHedRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ECSLXMLHedRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECSalesReportListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ECSalesReportListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECSalesReportRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ECSalesReportRow] = obj["value"]
      pass

class Erp_Tablesets_ECSLXMLDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ECSalesReportID:str = obj["ECSalesReportID"]
      """  European Sales List ID  """  
      self.LineNum:int = obj["LineNum"]
      self.SysEUMemState:str = obj["SysEUMemState"]
      self.UsrEUMemState:str = obj["UsrEUMemState"]
      self.SysCustomerVRN:str = obj["SysCustomerVRN"]
      self.UsrCustomerVRN:str = obj["UsrCustomerVRN"]
      self.CreateUser:str = obj["CreateUser"]
      """  Create User  """  
      self.ModifyUser:str = obj["ModifyUser"]
      """  Modify User  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Create Date  """  
      self.ModifyDate:str = obj["ModifyDate"]
      """  Modify Date  """  
      self.UsrValue:int = obj["UsrValue"]
      self.SysValue:int = obj["SysValue"]
      self.HedNum:int = obj["HedNum"]
      self.SysIndicator:str = obj["SysIndicator"]
      self.UsrIndicator:str = obj["UsrIndicator"]
      self.SysName:str = obj["SysName"]
      self.UsrName:str = obj["UsrName"]
      self.SysTaxValue:int = obj["SysTaxValue"]
      self.UsrTaxValue:int = obj["UsrTaxValue"]
      self.SysModule:str = obj["SysModule"]
      self.UsrModule:str = obj["UsrModule"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECSLXMLHedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ECSalesReportID:str = obj["ECSalesReportID"]
      """  European Sales List ID  """  
      self.SysSubmission:str = obj["SysSubmission"]
      self.UsrSubmission:str = obj["UsrSubmission"]
      self.SysTraderVRN:str = obj["SysTraderVRN"]
      """  UK VAT Registration Number (VRN).  """  
      self.UsrTraderVRN:str = obj["UsrTraderVRN"]
      """  UK VAT Registration Number (VRN).  """  
      self.SysYear:int = obj["SysYear"]
      self.UsrYear:int = obj["UsrYear"]
      self.SysPeriod:int = obj["SysPeriod"]
      self.UsrPeriod:int = obj["UsrPeriod"]
      self.SysCurrencyA3:str = obj["SysCurrencyA3"]
      self.UsrCurrencyA3:str = obj["UsrCurrencyA3"]
      self.SysContactName:str = obj["SysContactName"]
      self.UsrContactName:str = obj["UsrContactName"]
      self.SysOnline:int = obj["SysOnline"]
      self.UsrOnline:int = obj["UsrOnline"]
      self.SysBranch:int = obj["SysBranch"]
      """  Sys Branch  """  
      self.UsrBranch:int = obj["UsrBranch"]
      """  User Branch  """  
      self.CreateUser:str = obj["CreateUser"]
      """  Create User  """  
      self.ModifyUser:str = obj["ModifyUser"]
      """  Modify User  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Create Date  """  
      self.ModifyDate:str = obj["ModifyDate"]
      """  Modify Date  """  
      self.HedNum:int = obj["HedNum"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.UsrPhone:str = obj["UsrPhone"]
      """  UsrPhone  """  
      self.UsrEMailAddress:str = obj["UsrEMailAddress"]
      """  UsrEmailAddress  """  
      self.ColumnSeparator:str = obj["ColumnSeparator"]
      """  ColumnSeparator  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECSalesReportListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ECSalesReportID:str = obj["ECSalesReportID"]
      """  European Sales List ID  """  
      self.EndDate:str = obj["EndDate"]
      """  Report End Date  """  
      self.RangeOption:str = obj["RangeOption"]
      """  Range Option  """  
      self.RoundAmounts:bool = obj["RoundAmounts"]
      """  Round Amounts option  """  
      self.StartDate:str = obj["StartDate"]
      """  Start Date Report  """  
      self.TaxList:str = obj["TaxList"]
      self.VATTReportList:str = obj["VATTReportList"]
      self.Description:str = obj["Description"]
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  Unique identifier of the EFT. Related to EFTHead.EFTHeadUID.  """  
      self.OutputFile:str = obj["OutputFile"]
      """  This will be the default filename for the output file created by the electronic interface  """  
      self.ManualXML:bool = obj["ManualXML"]
      """  Field to identify manual changes on XML info.  """  
      self.Module:str = obj["Module"]
      """  Report Module parameter, options: AR or AR/AP  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EFTHeadName:str = obj["EFTHeadName"]
      """  Short name of the interface, it should be unique  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECSalesReportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ECSalesReportID:str = obj["ECSalesReportID"]
      """  European Sales List ID  """  
      self.EndDate:str = obj["EndDate"]
      """  Report End Date  """  
      self.RangeOption:str = obj["RangeOption"]
      """  Range Option  """  
      self.RoundAmounts:bool = obj["RoundAmounts"]
      """  Round Amounts option  """  
      self.StartDate:str = obj["StartDate"]
      """  Start Date Report  """  
      self.TaxList:str = obj["TaxList"]
      self.VATTReportList:str = obj["VATTReportList"]
      self.Description:str = obj["Description"]
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  Unique identifier of the EFT. Related to EFTHead.EFTHeadUID.  """  
      self.OutputFile:str = obj["OutputFile"]
      """  This will be the default filename for the output file created by the electronic interface  """  
      self.ManualXML:bool = obj["ManualXML"]
      """  Field to identify manual changes on XML info.  """  
      self.Module:str = obj["Module"]
      """  Report Module parameter, options: AR or AR/AP  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.InsideEUOnly:bool = obj["InsideEUOnly"]
      """  Sales outside the EU should not be included if any of the tax liabilities has the "Inside EU" flag checked  """  
      self.BEReportType:str = obj["BEReportType"]
      """  Report Type (CSF Belgium)  """  
      self.BERptLanguage:str = obj["BERptLanguage"]
      """  Report Language (CSF Belgium)  """  
      self.BEDspLimitAmount:int = obj["BEDspLimitAmount"]
      """  Display Limit Amount (CSF Belgium)  """  
      self.EndDateToken:str = obj["EndDateToken"]
      self.SortBy:str = obj["SortBy"]
      self.StartDateToken:str = obj["StartDateToken"]
      self.OutputFileNameDisplay:str = obj["OutputFileNameDisplay"]
      self.BitFlag:int = obj["BitFlag"]
      self.EFTHeadName:str = obj["EFTHeadName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   ecSalesReportID
   """  
   def __init__(self, obj):
      self.ecSalesReportID:str = obj["ecSalesReportID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_ECSLXMLDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ECSalesReportID:str = obj["ECSalesReportID"]
      """  European Sales List ID  """  
      self.LineNum:int = obj["LineNum"]
      self.SysEUMemState:str = obj["SysEUMemState"]
      self.UsrEUMemState:str = obj["UsrEUMemState"]
      self.SysCustomerVRN:str = obj["SysCustomerVRN"]
      self.UsrCustomerVRN:str = obj["UsrCustomerVRN"]
      self.CreateUser:str = obj["CreateUser"]
      """  Create User  """  
      self.ModifyUser:str = obj["ModifyUser"]
      """  Modify User  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Create Date  """  
      self.ModifyDate:str = obj["ModifyDate"]
      """  Modify Date  """  
      self.UsrValue:int = obj["UsrValue"]
      self.SysValue:int = obj["SysValue"]
      self.HedNum:int = obj["HedNum"]
      self.SysIndicator:str = obj["SysIndicator"]
      self.UsrIndicator:str = obj["UsrIndicator"]
      self.SysName:str = obj["SysName"]
      self.UsrName:str = obj["UsrName"]
      self.SysTaxValue:int = obj["SysTaxValue"]
      self.UsrTaxValue:int = obj["UsrTaxValue"]
      self.SysModule:str = obj["SysModule"]
      self.UsrModule:str = obj["UsrModule"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECSLXMLHedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ECSalesReportID:str = obj["ECSalesReportID"]
      """  European Sales List ID  """  
      self.SysSubmission:str = obj["SysSubmission"]
      self.UsrSubmission:str = obj["UsrSubmission"]
      self.SysTraderVRN:str = obj["SysTraderVRN"]
      """  UK VAT Registration Number (VRN).  """  
      self.UsrTraderVRN:str = obj["UsrTraderVRN"]
      """  UK VAT Registration Number (VRN).  """  
      self.SysYear:int = obj["SysYear"]
      self.UsrYear:int = obj["UsrYear"]
      self.SysPeriod:int = obj["SysPeriod"]
      self.UsrPeriod:int = obj["UsrPeriod"]
      self.SysCurrencyA3:str = obj["SysCurrencyA3"]
      self.UsrCurrencyA3:str = obj["UsrCurrencyA3"]
      self.SysContactName:str = obj["SysContactName"]
      self.UsrContactName:str = obj["UsrContactName"]
      self.SysOnline:int = obj["SysOnline"]
      self.UsrOnline:int = obj["UsrOnline"]
      self.SysBranch:int = obj["SysBranch"]
      """  Sys Branch  """  
      self.UsrBranch:int = obj["UsrBranch"]
      """  User Branch  """  
      self.CreateUser:str = obj["CreateUser"]
      """  Create User  """  
      self.ModifyUser:str = obj["ModifyUser"]
      """  Modify User  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Create Date  """  
      self.ModifyDate:str = obj["ModifyDate"]
      """  Modify Date  """  
      self.HedNum:int = obj["HedNum"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.UsrPhone:str = obj["UsrPhone"]
      """  UsrPhone  """  
      self.UsrEMailAddress:str = obj["UsrEMailAddress"]
      """  UsrEmailAddress  """  
      self.ColumnSeparator:str = obj["ColumnSeparator"]
      """  ColumnSeparator  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECSalesReportListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ECSalesReportID:str = obj["ECSalesReportID"]
      """  European Sales List ID  """  
      self.EndDate:str = obj["EndDate"]
      """  Report End Date  """  
      self.RangeOption:str = obj["RangeOption"]
      """  Range Option  """  
      self.RoundAmounts:bool = obj["RoundAmounts"]
      """  Round Amounts option  """  
      self.StartDate:str = obj["StartDate"]
      """  Start Date Report  """  
      self.TaxList:str = obj["TaxList"]
      self.VATTReportList:str = obj["VATTReportList"]
      self.Description:str = obj["Description"]
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  Unique identifier of the EFT. Related to EFTHead.EFTHeadUID.  """  
      self.OutputFile:str = obj["OutputFile"]
      """  This will be the default filename for the output file created by the electronic interface  """  
      self.ManualXML:bool = obj["ManualXML"]
      """  Field to identify manual changes on XML info.  """  
      self.Module:str = obj["Module"]
      """  Report Module parameter, options: AR or AR/AP  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EFTHeadName:str = obj["EFTHeadName"]
      """  Short name of the interface, it should be unique  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECSalesReportListTableset:
   def __init__(self, obj):
      self.ECSalesReportList:list[Erp_Tablesets_ECSalesReportListRow] = obj["ECSalesReportList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ECSalesReportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ECSalesReportID:str = obj["ECSalesReportID"]
      """  European Sales List ID  """  
      self.EndDate:str = obj["EndDate"]
      """  Report End Date  """  
      self.RangeOption:str = obj["RangeOption"]
      """  Range Option  """  
      self.RoundAmounts:bool = obj["RoundAmounts"]
      """  Round Amounts option  """  
      self.StartDate:str = obj["StartDate"]
      """  Start Date Report  """  
      self.TaxList:str = obj["TaxList"]
      self.VATTReportList:str = obj["VATTReportList"]
      self.Description:str = obj["Description"]
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  Unique identifier of the EFT. Related to EFTHead.EFTHeadUID.  """  
      self.OutputFile:str = obj["OutputFile"]
      """  This will be the default filename for the output file created by the electronic interface  """  
      self.ManualXML:bool = obj["ManualXML"]
      """  Field to identify manual changes on XML info.  """  
      self.Module:str = obj["Module"]
      """  Report Module parameter, options: AR or AR/AP  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.InsideEUOnly:bool = obj["InsideEUOnly"]
      """  Sales outside the EU should not be included if any of the tax liabilities has the "Inside EU" flag checked  """  
      self.BEReportType:str = obj["BEReportType"]
      """  Report Type (CSF Belgium)  """  
      self.BERptLanguage:str = obj["BERptLanguage"]
      """  Report Language (CSF Belgium)  """  
      self.BEDspLimitAmount:int = obj["BEDspLimitAmount"]
      """  Display Limit Amount (CSF Belgium)  """  
      self.EndDateToken:str = obj["EndDateToken"]
      self.SortBy:str = obj["SortBy"]
      self.StartDateToken:str = obj["StartDateToken"]
      self.OutputFileNameDisplay:str = obj["OutputFileNameDisplay"]
      self.BitFlag:int = obj["BitFlag"]
      self.EFTHeadName:str = obj["EFTHeadName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECSalesReportTableset:
   def __init__(self, obj):
      self.ECSalesReport:list[Erp_Tablesets_ECSalesReportRow] = obj["ECSalesReport"]
      self.ECSLXMLHed:list[Erp_Tablesets_ECSLXMLHedRow] = obj["ECSLXMLHed"]
      self.ECSLXMLDtl:list[Erp_Tablesets_ECSLXMLDtlRow] = obj["ECSLXMLDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtECSalesReportTableset:
   def __init__(self, obj):
      self.ECSalesReport:list[Erp_Tablesets_ECSalesReportRow] = obj["ECSalesReport"]
      self.ECSLXMLHed:list[Erp_Tablesets_ECSLXMLHedRow] = obj["ECSLXMLHed"]
      self.ECSLXMLDtl:list[Erp_Tablesets_ECSLXMLDtlRow] = obj["ECSLXMLDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ExportData_input:
   """ Required : 
   ipECSalesReportID
   """  
   def __init__(self, obj):
      self.ipECSalesReportID:str = obj["ipECSalesReportID"]
      """  ECSalesReportID  """  
      pass

class ExportData_output:
   def __init__(self, obj):
      pass

class GenerateXMLData_input:
   """ Required : 
   ipECSalesReportID
   ipManualXML
   """  
   def __init__(self, obj):
      self.ipECSalesReportID:str = obj["ipECSalesReportID"]
      """  ECSalesReportID  """  
      self.ipManualXML:bool = obj["ipManualXML"]
      """  ipManualXML  """  
      pass

class GenerateXMLData_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ECSalesReportTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   ecSalesReportID
   """  
   def __init__(self, obj):
      self.ecSalesReportID:str = obj["ecSalesReportID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ECSalesReportTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ECSalesReportTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ECSalesReportTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ECSalesReportListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewECSLXMLDtl_input:
   """ Required : 
   ds
   ecSalesReportID
   hedNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ECSalesReportTableset] = obj["ds"]
      self.ecSalesReportID:str = obj["ecSalesReportID"]
      self.hedNum:int = obj["hedNum"]
      pass

class GetNewECSLXMLDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ECSalesReportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewECSLXMLHed_input:
   """ Required : 
   ds
   ecSalesReportID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ECSalesReportTableset] = obj["ds"]
      self.ecSalesReportID:str = obj["ecSalesReportID"]
      pass

class GetNewECSLXMLHed_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ECSalesReportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewECSalesReport_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ECSalesReportTableset] = obj["ds"]
      pass

class GetNewECSalesReport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ECSalesReportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseECSalesReport
   whereClauseECSLXMLHed
   whereClauseECSLXMLDtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseECSalesReport:str = obj["whereClauseECSalesReport"]
      self.whereClauseECSLXMLHed:str = obj["whereClauseECSLXMLHed"]
      self.whereClauseECSLXMLDtl:str = obj["whereClauseECSLXMLDtl"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ECSalesReportTableset] = obj["returnObj"]
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

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtECSalesReportTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtECSalesReportTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ECSalesReportTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ECSalesReportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateECSLXMLDtl_input:
   """ Required : 
   ipECSalesReportID
   """  
   def __init__(self, obj):
      self.ipECSalesReportID:str = obj["ipECSalesReportID"]
      pass

class ValidateECSLXMLDtl_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.message:str = obj["parameters"]
      pass

      """  output parameters  """  

class ValidateEMail_input:
   """ Required : 
   email
   """  
   def __init__(self, obj):
      self.email:str = obj["email"]
      pass

class ValidateEMail_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.message:str = obj["parameters"]
      pass

      """  output parameters  """  

class ValidatePhone_input:
   """ Required : 
   phone
   """  
   def __init__(self, obj):
      self.phone:str = obj["phone"]
      pass

class ValidatePhone_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.message:str = obj["parameters"]
      pass

      """  output parameters  """  

