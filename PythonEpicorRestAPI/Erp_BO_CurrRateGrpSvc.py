import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.CurrRateGrpSvc
# Description: Currency Rates Group Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_CurrRateGrps(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CurrRateGrps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CurrRateGrps
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CurrRateGrpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrRateGrps",headers=creds) as resp:
           return await resp.json()

async def post_CurrRateGrps(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CurrRateGrps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CurrRateGrpRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CurrRateGrpRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrRateGrps", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CurrRateGrps_Company_RateGrpCode(Company, RateGrpCode, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CurrRateGrp item
   Description: Calls GetByID to retrieve the CurrRateGrp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CurrRateGrp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RateGrpCode: Desc: RateGrpCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CurrRateGrpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrRateGrps(" + Company + "," + RateGrpCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CurrRateGrps_Company_RateGrpCode(Company, RateGrpCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CurrRateGrp for the service
   Description: Calls UpdateExt to update CurrRateGrp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CurrRateGrp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RateGrpCode: Desc: RateGrpCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CurrRateGrpRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrRateGrps(" + Company + "," + RateGrpCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CurrRateGrps_Company_RateGrpCode(Company, RateGrpCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CurrRateGrp item
   Description: Call UpdateExt to delete CurrRateGrp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CurrRateGrp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RateGrpCode: Desc: RateGrpCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrRateGrps(" + Company + "," + RateGrpCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_CurrRateGrps_Company_RateGrpCode_CurrConvRules(Company, RateGrpCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get CurrConvRules items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CurrConvRules1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RateGrpCode: Desc: RateGrpCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CurrConvRuleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrRateGrps(" + Company + "," + RateGrpCode + ")/CurrConvRules",headers=creds) as resp:
           return await resp.json()

async def get_CurrRateGrps_Company_RateGrpCode_CurrConvRules_Company_RateGrpCode_SourceCurrCode_TargetCurrCode(Company, RateGrpCode, SourceCurrCode, TargetCurrCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CurrConvRule item
   Description: Calls GetByID to retrieve the CurrConvRule item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CurrConvRule1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RateGrpCode: Desc: RateGrpCode   Required: True   Allow empty value : True
      :param SourceCurrCode: Desc: SourceCurrCode   Required: True   Allow empty value : True
      :param TargetCurrCode: Desc: TargetCurrCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CurrConvRuleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrRateGrps(" + Company + "," + RateGrpCode + ")/CurrConvRules(" + Company + "," + RateGrpCode + "," + SourceCurrCode + "," + TargetCurrCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_CurrRateGrps_Company_RateGrpCode_CurrRateDisps(Company, RateGrpCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get CurrRateDisps items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CurrRateDisps1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RateGrpCode: Desc: RateGrpCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CurrRateDispRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrRateGrps(" + Company + "," + RateGrpCode + ")/CurrRateDisps",headers=creds) as resp:
           return await resp.json()

async def get_CurrRateGrps_Company_RateGrpCode_CurrRateDisps_Company_RateGrpCode_Seq(Company, RateGrpCode, Seq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CurrRateDisp item
   Description: Calls GetByID to retrieve the CurrRateDisp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CurrRateDisp1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RateGrpCode: Desc: RateGrpCode   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CurrRateDispRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrRateGrps(" + Company + "," + RateGrpCode + ")/CurrRateDisps(" + Company + "," + RateGrpCode + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def get_CurrRateGrps_Company_RateGrpCode_CurrRateGrpAttches(Company, RateGrpCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get CurrRateGrpAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CurrRateGrpAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RateGrpCode: Desc: RateGrpCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CurrRateGrpAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrRateGrps(" + Company + "," + RateGrpCode + ")/CurrRateGrpAttches",headers=creds) as resp:
           return await resp.json()

async def get_CurrRateGrps_Company_RateGrpCode_CurrRateGrpAttches_Company_RateGrpCode_DrawingSeq(Company, RateGrpCode, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CurrRateGrpAttch item
   Description: Calls GetByID to retrieve the CurrRateGrpAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CurrRateGrpAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RateGrpCode: Desc: RateGrpCode   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CurrRateGrpAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrRateGrps(" + Company + "," + RateGrpCode + ")/CurrRateGrpAttches(" + Company + "," + RateGrpCode + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_CurrConvRules(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CurrConvRules items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CurrConvRules
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CurrConvRuleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrConvRules",headers=creds) as resp:
           return await resp.json()

async def post_CurrConvRules(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CurrConvRules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CurrConvRuleRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CurrConvRuleRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrConvRules", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CurrConvRules_Company_RateGrpCode_SourceCurrCode_TargetCurrCode(Company, RateGrpCode, SourceCurrCode, TargetCurrCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CurrConvRule item
   Description: Calls GetByID to retrieve the CurrConvRule item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CurrConvRule
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RateGrpCode: Desc: RateGrpCode   Required: True   Allow empty value : True
      :param SourceCurrCode: Desc: SourceCurrCode   Required: True   Allow empty value : True
      :param TargetCurrCode: Desc: TargetCurrCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CurrConvRuleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrConvRules(" + Company + "," + RateGrpCode + "," + SourceCurrCode + "," + TargetCurrCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CurrConvRules_Company_RateGrpCode_SourceCurrCode_TargetCurrCode(Company, RateGrpCode, SourceCurrCode, TargetCurrCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CurrConvRule for the service
   Description: Calls UpdateExt to update CurrConvRule. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CurrConvRule
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RateGrpCode: Desc: RateGrpCode   Required: True   Allow empty value : True
      :param SourceCurrCode: Desc: SourceCurrCode   Required: True   Allow empty value : True
      :param TargetCurrCode: Desc: TargetCurrCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CurrConvRuleRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrConvRules(" + Company + "," + RateGrpCode + "," + SourceCurrCode + "," + TargetCurrCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CurrConvRules_Company_RateGrpCode_SourceCurrCode_TargetCurrCode(Company, RateGrpCode, SourceCurrCode, TargetCurrCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CurrConvRule item
   Description: Call UpdateExt to delete CurrConvRule item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CurrConvRule
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RateGrpCode: Desc: RateGrpCode   Required: True   Allow empty value : True
      :param SourceCurrCode: Desc: SourceCurrCode   Required: True   Allow empty value : True
      :param TargetCurrCode: Desc: TargetCurrCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrConvRules(" + Company + "," + RateGrpCode + "," + SourceCurrCode + "," + TargetCurrCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_CurrRateDisps(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CurrRateDisps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CurrRateDisps
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CurrRateDispRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrRateDisps",headers=creds) as resp:
           return await resp.json()

async def post_CurrRateDisps(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CurrRateDisps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CurrRateDispRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CurrRateDispRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrRateDisps", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CurrRateDisps_Company_RateGrpCode_Seq(Company, RateGrpCode, Seq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CurrRateDisp item
   Description: Calls GetByID to retrieve the CurrRateDisp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CurrRateDisp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RateGrpCode: Desc: RateGrpCode   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CurrRateDispRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrRateDisps(" + Company + "," + RateGrpCode + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CurrRateDisps_Company_RateGrpCode_Seq(Company, RateGrpCode, Seq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CurrRateDisp for the service
   Description: Calls UpdateExt to update CurrRateDisp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CurrRateDisp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RateGrpCode: Desc: RateGrpCode   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CurrRateDispRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrRateDisps(" + Company + "," + RateGrpCode + "," + Seq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CurrRateDisps_Company_RateGrpCode_Seq(Company, RateGrpCode, Seq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CurrRateDisp item
   Description: Call UpdateExt to delete CurrRateDisp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CurrRateDisp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RateGrpCode: Desc: RateGrpCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrRateDisps(" + Company + "," + RateGrpCode + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def get_CurrRateGrpAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CurrRateGrpAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CurrRateGrpAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CurrRateGrpAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrRateGrpAttches",headers=creds) as resp:
           return await resp.json()

async def post_CurrRateGrpAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CurrRateGrpAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CurrRateGrpAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CurrRateGrpAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrRateGrpAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CurrRateGrpAttches_Company_RateGrpCode_DrawingSeq(Company, RateGrpCode, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CurrRateGrpAttch item
   Description: Calls GetByID to retrieve the CurrRateGrpAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CurrRateGrpAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RateGrpCode: Desc: RateGrpCode   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CurrRateGrpAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrRateGrpAttches(" + Company + "," + RateGrpCode + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CurrRateGrpAttches_Company_RateGrpCode_DrawingSeq(Company, RateGrpCode, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CurrRateGrpAttch for the service
   Description: Calls UpdateExt to update CurrRateGrpAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CurrRateGrpAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RateGrpCode: Desc: RateGrpCode   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CurrRateGrpAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrRateGrpAttches(" + Company + "," + RateGrpCode + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CurrRateGrpAttches_Company_RateGrpCode_DrawingSeq(Company, RateGrpCode, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CurrRateGrpAttch item
   Description: Call UpdateExt to delete CurrRateGrpAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CurrRateGrpAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RateGrpCode: Desc: RateGrpCode   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/CurrRateGrpAttches(" + Company + "," + RateGrpCode + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CurrRateGrpListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseCurrRateGrp, whereClauseCurrRateGrpAttch, whereClauseCurrConvRule, whereClauseCurrRateDisp, pageSize, absolutePage, epicorHeaders = None):
   """  
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
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCurrRateGrp=" + whereClauseCurrRateGrp
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCurrRateGrpAttch=" + whereClauseCurrRateGrpAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCurrConvRule=" + whereClauseCurrConvRule
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCurrRateDisp=" + whereClauseCurrRateDisp
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(rateGrpCode, epicorHeaders = None):
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
   params += "rateGrpCode=" + rateGrpCode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_DefaultFieldsCurrConvRule(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultFieldsCurrConvRule
   OperationID: DefaultFieldsCurrConvRule
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultFieldsCurrConvRule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultFieldsCurrConvRule_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultFieldsCurrGrp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultFieldsCurrGrp
   OperationID: DefaultFieldsCurrGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultFieldsCurrGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultFieldsCurrGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCurrRateGrpForLink(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCurrRateGrpForLink
   Description: This returns the CurrRateGrp dataset for linking.
   OperationID: GetCurrRateGrpForLink
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCurrRateGrpForLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrRateGrpForLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetGlbCurrRateGrpList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetGlbCurrRateGrpList
   Description: This method returns the GlbCurrRateGrp dataset based on a delimited list of
GlbRateGrpCode values passed in.
   OperationID: GetGlbCurrRateGrpList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetGlbCurrRateGrpList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGlbCurrRateGrpList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LinkSelected(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LinkSelected
   OperationID: LinkSelected
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LinkSelected_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LinkSelected_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BuildGlbCurrRateGrpList(epicorHeaders = None):
   """  
   Summary: Invoke method BuildGlbCurrRateGrpList
   OperationID: BuildGlbCurrRateGrpList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildGlbCurrRateGrpList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GlbCurrRateGrpsExist(epicorHeaders = None):
   """  
   Summary: Invoke method GlbCurrRateGrpsExist
   Description: This method checks if GlbCurrRateGrp records exist or not.  Can be used
to determine if the option to link/unlink customers is available.
   OperationID: GlbCurrRateGrpsExist
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GlbCurrRateGrpsExist_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_CurrExRateExist(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CurrExRateExist
   Description: This method checks if CurrExRate records exist or not.
   OperationID: CurrExRateExist
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CurrExRateExist_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CurrExRateExist_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LinkGlbCurrRateGrp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LinkGlbCurrRateGrp
   Description: This method performs the actual logic behind linking a Currency Rate Group.  It is run after
the PreLinkGlbCurrRateGrp method which determines the Currency Rate Group Code to link to.
If the Currency Rate Group Code is for a Rate Group that already exists, the GlbCurrRateGrp information is
translated and then copied to the CurrRateGrpDataSet as an update.
If the Rate Group Code is for a new Rate Group, the GlbCurrRateGrp information is translated and then
copied to the CurrRateGrpDataSet as an Add.  Until the update method is run on CurrRateGrp record
the Link process is not completed.
   OperationID: LinkGlbCurrRateGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LinkGlbCurrRateGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LinkGlbCurrRateGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreLinkGlbCurrRateGrp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreLinkGlbCurrRateGrp
   Description: Linking a GlbCurrRateGrp record ties a global record to a new or existing CurrRateGrp record so
that any changes made to the GlbCurrRateGrp record in another company are automatically copied
to any linked Rate Groups.
This method performs the pre link logic to check of okay to link or get the new RateGrpCode
to create/link to.  Will be run before LinkGlbCurrRateGrp which actually creates/updates a
CurrRateGrp record and will send the modified record back for update.  When the Link "button" is
originally selected, the LinkRateGrpCode will be defaulted to the GlbRateGrpCode field.  It will then
check to see if this RateGrpCode is available for Use.  If available for use the system will return a
question asking the user if they want to use this code.  If the answer is no, then the user
either needs to select an existing rate group's code to link to or enter a brand new ID.  You will
run this method until the user answer is yes.  Then the LinkGlbCurrRateGrp method is called.
   OperationID: PreLinkGlbCurrRateGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreLinkGlbCurrRateGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreLinkGlbCurrRateGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SkipGlbCurrRateGrp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SkipGlbCurrRateGrp
   Description: This method performs the logic behind the skip option for GlbCurrRateGrp
Skip - sets the Skipped flag to true.
If the CurrRateGrpCode field is not blank will error out
   OperationID: SkipGlbCurrRateGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SkipGlbCurrRateGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SkipGlbCurrRateGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UnlinkGlbCurrRateGrp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UnlinkGlbCurrRateGrp
   Description: This method performs the logic behind the unlink option for GlbCurrRateGrp
Unlink - clears the RateGrpCode field in GlbCurrRateGrp.  Returns the CurrRateGrp DataSet
   OperationID: UnlinkGlbCurrRateGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnlinkGlbCurrRateGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnlinkGlbCurrRateGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateAltCrossCurrCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateAltCrossCurrCode
   Description: This method validates AltCrossCurrCode.
If exist at least one record on CurrConvRule with Rulecode value equal to  5 or 6
AltCrossCurrCode cannot be changed if exist at least one record on CurrConvRule with Rulecode value equal to 5 or 6
   OperationID: ValidateAltCrossCurrCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateAltCrossCurrCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateAltCrossCurrCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateBaseRateGrp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateBaseRateGrp
   Description: This method validates that:
(1) BaseRate must be a valid, active CurrRateGrp
(2) If this CurrRateGrp is used as a BaseRateGrp on any other CurrRateGrp then it's own BaseRateGrp cannot be populate.
(3) If choosing a BaseRateGrp, cannot choose a CurrRateGrp that has a BaseRateGrp defined.
(4) If any Conversion Rule (currConvRule) have their UseBaseRate set to true, cannot clear BaseRateGrp field.
   OperationID: ValidateBaseRateGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateBaseRateGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateBaseRateGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateCrossCurrCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateCrossCurrCode
   Description: This method validates if exist at least one record on CurrConvRule with Rulecode value equal to 3, 4, 5 or 6
CrossCurrCode cannot be changed if exist at least one record on CurrConvRule with Rulecode value equal to 3, 4, 5 or 6
   OperationID: ValidateCrossCurrCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateCrossCurrCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCrossCurrCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateCurrencies(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateCurrencies
   Description: Validate that when changing the cross rate currencies on a RateGrp
if BaseRateGrp is defined must validate against the BaseRateGrp's currencies
if it is used as a BaseRateGrp on other RateGrps (could be more than one) must validate against the RateGrps' currencies
   OperationID: ValidateCurrencies
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateCurrencies_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCurrencies_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateInactive(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateInactive
   Description: This method validate , that  CurrRateGrp.Inactive cannot be marked as true
if the rate group is assigned to a Company Default.
   OperationID: ValidateInactive
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateInactive_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateInactive_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateRateGrpCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateRateGrpCode
   Description: This method validate , that  RateGrpCode is unique
   OperationID: ValidateRateGrpCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateRateGrpCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateRateGrpCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateRateGrpDescription(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateRateGrpDescription
   Description: This method validate , that  Description is unique
   OperationID: ValidateRateGrpDescription
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateRateGrpDescription_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateRateGrpDescription_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateRateNumDec(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateRateNumDec
   Description: This method validate , that  RateNumDec not exceed 6 decimal places
   OperationID: ValidateRateNumDec
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateRateNumDec_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateRateNumDec_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateRuleCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateRuleCode
   OperationID: ValidateRuleCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateRuleCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateRuleCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateUseBaseRate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateUseBaseRate
   OperationID: ValidateUseBaseRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateUseBaseRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateUseBaseRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_validateExCurrStatusForRateType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method validateExCurrStatusForRateType
   Description: This method validates the current status for the Rate Group that will be linked to a global Rate Type
   OperationID: validateExCurrStatusForRateType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/validateExCurrStatusForRateType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/validateExCurrStatusForRateType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCurrRateGrp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCurrRateGrp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCurrRateGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCurrRateGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCurrRateGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCurrRateGrpAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCurrRateGrpAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCurrRateGrpAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCurrRateGrpAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCurrRateGrpAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCurrConvRule(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCurrConvRule
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCurrConvRule
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCurrConvRule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCurrConvRule_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCurrRateDisp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCurrRateDisp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCurrRateDisp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCurrRateDisp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCurrRateDisp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrRateGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrConvRuleRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CurrConvRuleRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrRateDispRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CurrRateDispRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrRateGrpAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CurrRateGrpAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrRateGrpListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CurrRateGrpListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrRateGrpRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CurrRateGrpRow] = obj["value"]
      pass

class Erp_Tablesets_CurrConvRuleRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SourceCurrCode:str = obj["SourceCurrCode"]
      """  A unique code that identifies the source currency.  """  
      self.TargetCurrCode:str = obj["TargetCurrCode"]
      """  A unique code that identifies the target currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.UseBaseRate:bool = obj["UseBaseRate"]
      """  Determine if the user should use the base rate group defined in CurrRateGrp  """  
      self.RuleCode:int = obj["RuleCode"]
      """  Indicates the type of conversion rule. Direct, Inverse, Cross Rate, Reverse Cross Rate, Double Cross Rate or Reverse Double Cross Rate  """  
      self.FixedRate:bool = obj["FixedRate"]
      """  Indiates if the exchange rate is fixed and cannot be updated  """  
      self.DisplayMode:int = obj["DisplayMode"]
      """  Indicates which exchange rate to display/update on the transaction  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SourceTargetCode:str = obj["SourceTargetCode"]
      """  This field is used as display on the Three Node. Is compose by the source and target code separated by an hyphen (-) . i.e. XXXX-XXX  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the Currency Rate Group is Global (master or linked)  """  
      self.SouceCurrDspID:str = obj["SouceCurrDspID"]
      """  Souce Currency ID with Scale Factor  """  
      self.TargetCurrDspID:str = obj["TargetCurrDspID"]
      """  Target Currency ID wiht Scale Factor  """  
      self.DisplayModeText:str = obj["DisplayModeText"]
      self.RuleCodeText:str = obj["RuleCodeText"]
      self.BitFlag:int = obj["BitFlag"]
      self.SourceCurrCurrName:str = obj["SourceCurrCurrName"]
      self.SourceCurrCurrDesc:str = obj["SourceCurrCurrDesc"]
      self.SourceCurrDocumentDesc:str = obj["SourceCurrDocumentDesc"]
      self.SourceCurrCurrSymbol:str = obj["SourceCurrCurrSymbol"]
      self.SourceCurrCurrencyID:str = obj["SourceCurrCurrencyID"]
      self.TargetCurrCurrDesc:str = obj["TargetCurrCurrDesc"]
      self.TargetCurrDocumentDesc:str = obj["TargetCurrDocumentDesc"]
      self.TargetCurrCurrName:str = obj["TargetCurrCurrName"]
      self.TargetCurrCurrencyID:str = obj["TargetCurrCurrencyID"]
      self.TargetCurrCurrSymbol:str = obj["TargetCurrCurrSymbol"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CurrRateDispRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.Seq:int = obj["Seq"]
      """  Order in which the currencies should be displayed in the matrix grids  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency code to be displayed  """  
      self.ScaleFactor:int = obj["ScaleFactor"]
      """  Display factor for exchange rates  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the Currency Rate Group is Global (master or linked)  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CurrRateGrpAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.RateGrpCode:str = obj["RateGrpCode"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CurrRateGrpListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Inactive:bool = obj["Inactive"]
      """  Determines if the record is inactive  """  
      self.BaseRateGrpCode:str = obj["BaseRateGrpCode"]
      """  Determins if there is a base rate group to use if no rules or rates are defined for a currency  """  
      self.CrossCurrCode:str = obj["CrossCurrCode"]
      """  Currency to use during single or double currency conversions  """  
      self.CrossRound:bool = obj["CrossRound"]
      """  Determine if rounding should be done after conversion  """  
      self.CrossRoundDec:int = obj["CrossRoundDec"]
      """  Number of decimals to use during rounding  """  
      self.AltCrossCurrCode:str = obj["AltCrossCurrCode"]
      """  Currency used for double currency conversions  """  
      self.AltCrossRound:bool = obj["AltCrossRound"]
      """  Determine if rounding should be done after conversion  """  
      self.AltCrossRoundDec:int = obj["AltCrossRoundDec"]
      """  Number of decimals to use during rounding  """  
      self.GlobalGrp:bool = obj["GlobalGrp"]
      """  Determines whether or not this rate group is shared between more than one company.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Determines whether or not this record will receive global updates.  """  
      self.RateNumDec:int = obj["RateNumDec"]
      """  Number of decimals for the exchange rates  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EnableGlobalGrp:bool = obj["EnableGlobalGrp"]
      """  control when the GlobalGrp field should be enabled.  """  
      self.EnableGlobalLock:bool = obj["EnableGlobalLock"]
      """  Control when the GlobalLock field should be enabled.  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the Currency is Global (master or linked)  """  
      self.GlbLink:str = obj["GlbLink"]
      """  Delimited list of GlbCompany and GlbRateGrpCode that is linking to this Rate Group.  """  
      self.AltCrossCurrCurrDesc:str = obj["AltCrossCurrCurrDesc"]
      """  Description of the currency  """  
      self.AltCrossCurrCurrSymbol:str = obj["AltCrossCurrCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.AltCrossCurrCurrencyID:str = obj["AltCrossCurrCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.AltCrossCurrDocumentDesc:str = obj["AltCrossCurrDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.AltCrossCurrCurrName:str = obj["AltCrossCurrCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.BaseRateGrpDescDescription:str = obj["BaseRateGrpDescDescription"]
      """  Description  """  
      self.CrossCurrCurrDesc:str = obj["CrossCurrCurrDesc"]
      """  Description of the currency  """  
      self.CrossCurrCurrSymbol:str = obj["CrossCurrCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CrossCurrCurrencyID:str = obj["CrossCurrCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CrossCurrDocumentDesc:str = obj["CrossCurrDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CrossCurrCurrName:str = obj["CrossCurrCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CurrRateGrpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Inactive:bool = obj["Inactive"]
      """  Determines if the record is inactive  """  
      self.BaseRateGrpCode:str = obj["BaseRateGrpCode"]
      """  Determins if there is a base rate group to use if no rules or rates are defined for a currency  """  
      self.CrossCurrCode:str = obj["CrossCurrCode"]
      """  Currency to use during single or double currency conversions  """  
      self.CrossRound:bool = obj["CrossRound"]
      """  Determine if rounding should be done after conversion  """  
      self.CrossRoundDec:int = obj["CrossRoundDec"]
      """  Number of decimals to use during rounding  """  
      self.AltCrossCurrCode:str = obj["AltCrossCurrCode"]
      """  Currency used for double currency conversions  """  
      self.AltCrossRound:bool = obj["AltCrossRound"]
      """  Determine if rounding should be done after conversion  """  
      self.AltCrossRoundDec:int = obj["AltCrossRoundDec"]
      """  Number of decimals to use during rounding  """  
      self.GlobalGrp:bool = obj["GlobalGrp"]
      """  Determines whether or not this rate group is shared between more than one company.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Determines whether or not this record will receive global updates.  """  
      self.RateNumDec:int = obj["RateNumDec"]
      """  Number of decimals for the exchange rates  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EnableGlobalGrp:bool = obj["EnableGlobalGrp"]
      """  control when the GlobalGrp field should be enabled.  """  
      self.EnableGlobalLock:bool = obj["EnableGlobalLock"]
      """  Control when the GlobalLock field should be enabled.  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the Currency is Global (master or linked)  """  
      self.GlbLink:str = obj["GlbLink"]
      """  Delimited list of GlbCompany and GlbRateGrpCode that is linking to this Rate Group.  """  
      self.GlbCompanyName:str = obj["GlbCompanyName"]
      """  Company Name from linked global rate group.  """  
      self.GlbRateGrpCode:str = obj["GlbRateGrpCode"]
      """  Rate group Code from linked global rate group.  """  
      self.GlbRateGrpDesc:str = obj["GlbRateGrpDesc"]
      """  Description from linked global rate group.  """  
      self.GlbCompanyID:str = obj["GlbCompanyID"]
      """  Company ID from linked global rate group.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AltCrossCurrCurrName:str = obj["AltCrossCurrCurrName"]
      self.AltCrossCurrCurrDesc:str = obj["AltCrossCurrCurrDesc"]
      self.AltCrossCurrCurrencyID:str = obj["AltCrossCurrCurrencyID"]
      self.AltCrossCurrDocumentDesc:str = obj["AltCrossCurrDocumentDesc"]
      self.AltCrossCurrCurrSymbol:str = obj["AltCrossCurrCurrSymbol"]
      self.BaseRateGrpDescDescription:str = obj["BaseRateGrpDescDescription"]
      self.CrossCurrCurrDesc:str = obj["CrossCurrCurrDesc"]
      self.CrossCurrCurrName:str = obj["CrossCurrCurrName"]
      self.CrossCurrCurrencyID:str = obj["CrossCurrCurrencyID"]
      self.CrossCurrDocumentDesc:str = obj["CrossCurrDocumentDesc"]
      self.CrossCurrCurrSymbol:str = obj["CrossCurrCurrSymbol"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class BuildGlbCurrRateGrpList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GlbCurrRateGrpTableset] = obj["returnObj"]
      pass

class CurrExRateExist_input:
   """ Required : 
   pRateGrpCode
   """  
   def __init__(self, obj):
      self.pRateGrpCode:str = obj["pRateGrpCode"]
      """  Rate Group code.  """  
      pass

class CurrExRateExist_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pCurrExRateExist:bool = obj["pCurrExRateExist"]
      pass

      """  output parameters  """  

class DefaultFieldsCurrConvRule_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CurrRateGrpTableset] = obj["ds"]
      pass

class DefaultFieldsCurrConvRule_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CurrRateGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DefaultFieldsCurrGrp_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CurrRateGrpTableset] = obj["ds"]
      pass

class DefaultFieldsCurrGrp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CurrRateGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   rateGrpCode
   """  
   def __init__(self, obj):
      self.rateGrpCode:str = obj["rateGrpCode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_CurrConvRuleRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SourceCurrCode:str = obj["SourceCurrCode"]
      """  A unique code that identifies the source currency.  """  
      self.TargetCurrCode:str = obj["TargetCurrCode"]
      """  A unique code that identifies the target currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.UseBaseRate:bool = obj["UseBaseRate"]
      """  Determine if the user should use the base rate group defined in CurrRateGrp  """  
      self.RuleCode:int = obj["RuleCode"]
      """  Indicates the type of conversion rule. Direct, Inverse, Cross Rate, Reverse Cross Rate, Double Cross Rate or Reverse Double Cross Rate  """  
      self.FixedRate:bool = obj["FixedRate"]
      """  Indiates if the exchange rate is fixed and cannot be updated  """  
      self.DisplayMode:int = obj["DisplayMode"]
      """  Indicates which exchange rate to display/update on the transaction  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SourceTargetCode:str = obj["SourceTargetCode"]
      """  This field is used as display on the Three Node. Is compose by the source and target code separated by an hyphen (-) . i.e. XXXX-XXX  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the Currency Rate Group is Global (master or linked)  """  
      self.SouceCurrDspID:str = obj["SouceCurrDspID"]
      """  Souce Currency ID with Scale Factor  """  
      self.TargetCurrDspID:str = obj["TargetCurrDspID"]
      """  Target Currency ID wiht Scale Factor  """  
      self.DisplayModeText:str = obj["DisplayModeText"]
      self.RuleCodeText:str = obj["RuleCodeText"]
      self.BitFlag:int = obj["BitFlag"]
      self.SourceCurrCurrName:str = obj["SourceCurrCurrName"]
      self.SourceCurrCurrDesc:str = obj["SourceCurrCurrDesc"]
      self.SourceCurrDocumentDesc:str = obj["SourceCurrDocumentDesc"]
      self.SourceCurrCurrSymbol:str = obj["SourceCurrCurrSymbol"]
      self.SourceCurrCurrencyID:str = obj["SourceCurrCurrencyID"]
      self.TargetCurrCurrDesc:str = obj["TargetCurrCurrDesc"]
      self.TargetCurrDocumentDesc:str = obj["TargetCurrDocumentDesc"]
      self.TargetCurrCurrName:str = obj["TargetCurrCurrName"]
      self.TargetCurrCurrencyID:str = obj["TargetCurrCurrencyID"]
      self.TargetCurrCurrSymbol:str = obj["TargetCurrCurrSymbol"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CurrRateDispRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.Seq:int = obj["Seq"]
      """  Order in which the currencies should be displayed in the matrix grids  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency code to be displayed  """  
      self.ScaleFactor:int = obj["ScaleFactor"]
      """  Display factor for exchange rates  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the Currency Rate Group is Global (master or linked)  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CurrRateGrpAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.RateGrpCode:str = obj["RateGrpCode"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CurrRateGrpListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Inactive:bool = obj["Inactive"]
      """  Determines if the record is inactive  """  
      self.BaseRateGrpCode:str = obj["BaseRateGrpCode"]
      """  Determins if there is a base rate group to use if no rules or rates are defined for a currency  """  
      self.CrossCurrCode:str = obj["CrossCurrCode"]
      """  Currency to use during single or double currency conversions  """  
      self.CrossRound:bool = obj["CrossRound"]
      """  Determine if rounding should be done after conversion  """  
      self.CrossRoundDec:int = obj["CrossRoundDec"]
      """  Number of decimals to use during rounding  """  
      self.AltCrossCurrCode:str = obj["AltCrossCurrCode"]
      """  Currency used for double currency conversions  """  
      self.AltCrossRound:bool = obj["AltCrossRound"]
      """  Determine if rounding should be done after conversion  """  
      self.AltCrossRoundDec:int = obj["AltCrossRoundDec"]
      """  Number of decimals to use during rounding  """  
      self.GlobalGrp:bool = obj["GlobalGrp"]
      """  Determines whether or not this rate group is shared between more than one company.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Determines whether or not this record will receive global updates.  """  
      self.RateNumDec:int = obj["RateNumDec"]
      """  Number of decimals for the exchange rates  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EnableGlobalGrp:bool = obj["EnableGlobalGrp"]
      """  control when the GlobalGrp field should be enabled.  """  
      self.EnableGlobalLock:bool = obj["EnableGlobalLock"]
      """  Control when the GlobalLock field should be enabled.  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the Currency is Global (master or linked)  """  
      self.GlbLink:str = obj["GlbLink"]
      """  Delimited list of GlbCompany and GlbRateGrpCode that is linking to this Rate Group.  """  
      self.AltCrossCurrCurrDesc:str = obj["AltCrossCurrCurrDesc"]
      """  Description of the currency  """  
      self.AltCrossCurrCurrSymbol:str = obj["AltCrossCurrCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.AltCrossCurrCurrencyID:str = obj["AltCrossCurrCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.AltCrossCurrDocumentDesc:str = obj["AltCrossCurrDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.AltCrossCurrCurrName:str = obj["AltCrossCurrCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.BaseRateGrpDescDescription:str = obj["BaseRateGrpDescDescription"]
      """  Description  """  
      self.CrossCurrCurrDesc:str = obj["CrossCurrCurrDesc"]
      """  Description of the currency  """  
      self.CrossCurrCurrSymbol:str = obj["CrossCurrCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CrossCurrCurrencyID:str = obj["CrossCurrCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CrossCurrDocumentDesc:str = obj["CrossCurrDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CrossCurrCurrName:str = obj["CrossCurrCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CurrRateGrpListTableset:
   def __init__(self, obj):
      self.CurrRateGrpList:list[Erp_Tablesets_CurrRateGrpListRow] = obj["CurrRateGrpList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CurrRateGrpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Inactive:bool = obj["Inactive"]
      """  Determines if the record is inactive  """  
      self.BaseRateGrpCode:str = obj["BaseRateGrpCode"]
      """  Determins if there is a base rate group to use if no rules or rates are defined for a currency  """  
      self.CrossCurrCode:str = obj["CrossCurrCode"]
      """  Currency to use during single or double currency conversions  """  
      self.CrossRound:bool = obj["CrossRound"]
      """  Determine if rounding should be done after conversion  """  
      self.CrossRoundDec:int = obj["CrossRoundDec"]
      """  Number of decimals to use during rounding  """  
      self.AltCrossCurrCode:str = obj["AltCrossCurrCode"]
      """  Currency used for double currency conversions  """  
      self.AltCrossRound:bool = obj["AltCrossRound"]
      """  Determine if rounding should be done after conversion  """  
      self.AltCrossRoundDec:int = obj["AltCrossRoundDec"]
      """  Number of decimals to use during rounding  """  
      self.GlobalGrp:bool = obj["GlobalGrp"]
      """  Determines whether or not this rate group is shared between more than one company.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Determines whether or not this record will receive global updates.  """  
      self.RateNumDec:int = obj["RateNumDec"]
      """  Number of decimals for the exchange rates  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EnableGlobalGrp:bool = obj["EnableGlobalGrp"]
      """  control when the GlobalGrp field should be enabled.  """  
      self.EnableGlobalLock:bool = obj["EnableGlobalLock"]
      """  Control when the GlobalLock field should be enabled.  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the Currency is Global (master or linked)  """  
      self.GlbLink:str = obj["GlbLink"]
      """  Delimited list of GlbCompany and GlbRateGrpCode that is linking to this Rate Group.  """  
      self.GlbCompanyName:str = obj["GlbCompanyName"]
      """  Company Name from linked global rate group.  """  
      self.GlbRateGrpCode:str = obj["GlbRateGrpCode"]
      """  Rate group Code from linked global rate group.  """  
      self.GlbRateGrpDesc:str = obj["GlbRateGrpDesc"]
      """  Description from linked global rate group.  """  
      self.GlbCompanyID:str = obj["GlbCompanyID"]
      """  Company ID from linked global rate group.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AltCrossCurrCurrName:str = obj["AltCrossCurrCurrName"]
      self.AltCrossCurrCurrDesc:str = obj["AltCrossCurrCurrDesc"]
      self.AltCrossCurrCurrencyID:str = obj["AltCrossCurrCurrencyID"]
      self.AltCrossCurrDocumentDesc:str = obj["AltCrossCurrDocumentDesc"]
      self.AltCrossCurrCurrSymbol:str = obj["AltCrossCurrCurrSymbol"]
      self.BaseRateGrpDescDescription:str = obj["BaseRateGrpDescDescription"]
      self.CrossCurrCurrDesc:str = obj["CrossCurrCurrDesc"]
      self.CrossCurrCurrName:str = obj["CrossCurrCurrName"]
      self.CrossCurrCurrencyID:str = obj["CrossCurrCurrencyID"]
      self.CrossCurrDocumentDesc:str = obj["CrossCurrDocumentDesc"]
      self.CrossCurrCurrSymbol:str = obj["CrossCurrCurrSymbol"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CurrRateGrpTableset:
   def __init__(self, obj):
      self.CurrRateGrp:list[Erp_Tablesets_CurrRateGrpRow] = obj["CurrRateGrp"]
      self.CurrRateGrpAttch:list[Erp_Tablesets_CurrRateGrpAttchRow] = obj["CurrRateGrpAttch"]
      self.CurrConvRule:list[Erp_Tablesets_CurrConvRuleRow] = obj["CurrConvRule"]
      self.CurrRateDisp:list[Erp_Tablesets_CurrRateDispRow] = obj["CurrRateDisp"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GlbCurrConvRuleRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SourceCurrCode:str = obj["SourceCurrCode"]
      """  A unique code that identifies the source currency.  """  
      self.TargetCurrCode:str = obj["TargetCurrCode"]
      """  A unique code that identifies the target currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.UseBaseRate:bool = obj["UseBaseRate"]
      """  Determine if the user should use the base rate group defined in CurrRateGrp  """  
      self.RuleCode:int = obj["RuleCode"]
      """  Indicates the type of conversion rule. Direct, Inverse, Cross Rate, Reverse Cross Rate, Double Cross Rate or Reverse Double Cross Rate  """  
      self.FixedRate:bool = obj["FixedRate"]
      """  Indiates if the exchange rate is fixed and cannot be updated  """  
      self.GlbRateGrpCode:str = obj["GlbRateGrpCode"]
      """  Currency Rate Group Code from Source Company  """  
      self.GlbSourceCurrCode:str = obj["GlbSourceCurrCode"]
      """  Source Currency from Source Company  """  
      self.GlbTargetCurrCode:str = obj["GlbTargetCurrCode"]
      """  Target Currency from Source Company  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Source Company  """  
      self.DisplayMode:int = obj["DisplayMode"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the Currency Rate Group is Global (master or linked)  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GlbCurrExRateRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SourceCurrCode:str = obj["SourceCurrCode"]
      """  A unique code that identifies the source currency.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  This rate is effective as of this date.  """  
      self.CurrentRate:int = obj["CurrentRate"]
      """   Current Rate will be the default used by the system.
Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was modified.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was modified.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It can not be overridden.  """  
      self.Reference:str = obj["Reference"]
      """  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  """  
      self.TargetCurrCode:str = obj["TargetCurrCode"]
      """  A unique code that identifies the target currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.GlbRateGrpCode:str = obj["GlbRateGrpCode"]
      """  Currency Rate Group Code from Source Company  """  
      self.GlbSourceCurrCode:str = obj["GlbSourceCurrCode"]
      """  Source Currency from Source Company  """  
      self.GlbTargetCurrCode:str = obj["GlbTargetCurrCode"]
      """  Target Currency from Source Company  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Source Company  """  
      self.GlbEffectiveDate:str = obj["GlbEffectiveDate"]
      """  Effective Date from Source Company  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the Currency Rate Group is Global (master or linked)  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GlbCurrRateDispRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.Seq:int = obj["Seq"]
      """  Order in which the currencies should be displayed in the matrix grids  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency code to be displayed  """  
      self.GlbRateGrpCode:str = obj["GlbRateGrpCode"]
      """  Currency Rate Group Code from source company  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Source Company  """  
      self.GlbSeq:int = obj["GlbSeq"]
      """  Sequence from Source Company  """  
      self.ScaleFactor:int = obj["ScaleFactor"]
      """  Display factor for exchange rates  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the Currency Rate Group is Global (master or linked)  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GlbCurrRateGrpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GlbRateGrpCode:str = obj["GlbRateGrpCode"]
      """  Currency Rate Group Code from source company  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Source Company  """  
      self.Skipped:bool = obj["Skipped"]
      """  Indicates that the user has reviewed the record but its not going to be linked currently  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Inactive:bool = obj["Inactive"]
      """  Determines if the record is inactive  """  
      self.BaseRateGrpCode:str = obj["BaseRateGrpCode"]
      """  Determins if there is a base rate group to use if no rules or rates are defined for a currency  """  
      self.CrossCurrCode:str = obj["CrossCurrCode"]
      """  Currency to use during single or double currency conversions  """  
      self.CrossRound:bool = obj["CrossRound"]
      """  Determine if rounding should be done after conversion  """  
      self.CrossRoundDec:int = obj["CrossRoundDec"]
      """  Number of decimals to use during rounding  """  
      self.AltCrossCurrCode:str = obj["AltCrossCurrCode"]
      """  Currency used for double currency conversions  """  
      self.AltCrossRound:bool = obj["AltCrossRound"]
      """  Determine if rounding should be done after conversion  """  
      self.AltCrossRoundDec:int = obj["AltCrossRoundDec"]
      """  Number of decimals to use during rounding  """  
      self.GlobalGrp:bool = obj["GlobalGrp"]
      """  Determines whether or not this rate group is shared between more than one company.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Determines whether or not this record will receive global updates.  """  
      self.DisplayMode:int = obj["DisplayMode"]
      """  Indicates which exchange rate to display/update on the transaction  """  
      self.RateNumDec:int = obj["RateNumDec"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.LinkRateGrpCode:str = obj["LinkRateGrpCode"]
      """  CurrRateGrp.RateGrpCode to link to (new or existing)  """  
      self.LocalDesc:str = obj["LocalDesc"]
      """  holds description of currency rate group from local rate group linked.  """  
      self.Select:bool = obj["Select"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GlbCurrRateGrpTableset:
   def __init__(self, obj):
      self.GlbCurrRateGrp:list[Erp_Tablesets_GlbCurrRateGrpRow] = obj["GlbCurrRateGrp"]
      self.GlbCurrConvRule:list[Erp_Tablesets_GlbCurrConvRuleRow] = obj["GlbCurrConvRule"]
      self.GlbCurrExRate:list[Erp_Tablesets_GlbCurrExRateRow] = obj["GlbCurrExRate"]
      self.GlbCurrRateDisp:list[Erp_Tablesets_GlbCurrRateDispRow] = obj["GlbCurrRateDisp"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtCurrRateGrpTableset:
   def __init__(self, obj):
      self.CurrRateGrp:list[Erp_Tablesets_CurrRateGrpRow] = obj["CurrRateGrp"]
      self.CurrRateGrpAttch:list[Erp_Tablesets_CurrRateGrpAttchRow] = obj["CurrRateGrpAttch"]
      self.CurrConvRule:list[Erp_Tablesets_CurrConvRuleRow] = obj["CurrConvRule"]
      self.CurrRateDisp:list[Erp_Tablesets_CurrRateDispRow] = obj["CurrRateDisp"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   rateGrpCode
   """  
   def __init__(self, obj):
      self.rateGrpCode:str = obj["rateGrpCode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CurrRateGrpTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CurrRateGrpTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CurrRateGrpTableset] = obj["returnObj"]
      pass

class GetCurrRateGrpForLink_input:
   """ Required : 
   currRateGrpCode
   """  
   def __init__(self, obj):
      self.currRateGrpCode:str = obj["currRateGrpCode"]
      """  Global Rate Group Code GLBCurrRateGrp record to link  """  
      pass

class GetCurrRateGrpForLink_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CurrRateGrpTableset] = obj["returnObj"]
      pass

class GetGlbCurrRateGrpList_input:
   """ Required : 
   glbRateGrpCodeList
   """  
   def __init__(self, obj):
      self.glbRateGrpCodeList:str = obj["glbRateGrpCodeList"]
      """  Delimited list of glbRateGrpCode values  """  
      pass

class GetGlbCurrRateGrpList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GlbCurrRateGrpTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CurrRateGrpListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewCurrConvRule_input:
   """ Required : 
   ds
   rateGrpCode
   sourceCurrCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CurrRateGrpTableset] = obj["ds"]
      self.rateGrpCode:str = obj["rateGrpCode"]
      self.sourceCurrCode:str = obj["sourceCurrCode"]
      pass

class GetNewCurrConvRule_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CurrRateGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCurrRateDisp_input:
   """ Required : 
   ds
   rateGrpCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CurrRateGrpTableset] = obj["ds"]
      self.rateGrpCode:str = obj["rateGrpCode"]
      pass

class GetNewCurrRateDisp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CurrRateGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCurrRateGrpAttch_input:
   """ Required : 
   ds
   rateGrpCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CurrRateGrpTableset] = obj["ds"]
      self.rateGrpCode:str = obj["rateGrpCode"]
      pass

class GetNewCurrRateGrpAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CurrRateGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCurrRateGrp_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CurrRateGrpTableset] = obj["ds"]
      pass

class GetNewCurrRateGrp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CurrRateGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseCurrRateGrp
   whereClauseCurrRateGrpAttch
   whereClauseCurrConvRule
   whereClauseCurrRateDisp
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCurrRateGrp:str = obj["whereClauseCurrRateGrp"]
      self.whereClauseCurrRateGrpAttch:str = obj["whereClauseCurrRateGrpAttch"]
      self.whereClauseCurrConvRule:str = obj["whereClauseCurrConvRule"]
      self.whereClauseCurrRateDisp:str = obj["whereClauseCurrRateDisp"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CurrRateGrpTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GlbCurrRateGrpsExist_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.GlbCurrRateGrpsExist:bool = obj["GlbCurrRateGrpsExist"]
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

class LinkGlbCurrRateGrp_input:
   """ Required : 
   glbCompany
   glbRateGrpCode
   ds
   ds1
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      """  Global Company field on the GlbCurrRateGrp record to link  """  
      self.glbRateGrpCode:str = obj["glbRateGrpCode"]
      """  Global CurrRateGrp Code field on the GlbCurrRateGrp record to link  """  
      self.ds:list[Erp_Tablesets_GlbCurrRateGrpTableset] = obj["ds"]
      self.ds1:list[Erp_Tablesets_CurrRateGrpTableset] = obj["ds1"]
      pass

class LinkGlbCurrRateGrp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlbCurrRateGrpTableset] = obj["ds"]
      self.ds1:list[Erp_Tablesets_CurrRateGrpTableset] = obj["ds1"]
      pass

      """  output parameters  """  

class LinkSelected_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GlbCurrRateGrpTableset] = obj["ds"]
      pass

class LinkSelected_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.linkEnable:bool = obj["linkEnable"]
      self.unLinlkEnable:bool = obj["unLinlkEnable"]
      self.ds:list[Erp_Tablesets_GlbCurrRateGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PreLinkGlbCurrRateGrp_input:
   """ Required : 
   glbCompany
   glbRateGrpCode
   ds
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      """  Global Company field on the GlbCurrRateGrp record to link  """  
      self.glbRateGrpCode:str = obj["glbRateGrpCode"]
      """  Global Rate Group Code field on the GlbCurrRateGrp record to link  """  
      self.ds:list[Erp_Tablesets_GlbCurrRateGrpTableset] = obj["ds"]
      pass

class PreLinkGlbCurrRateGrp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlbCurrRateGrpTableset] = obj["ds"]
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class SkipGlbCurrRateGrp_input:
   """ Required : 
   glbCompany
   glbRateGrpCode
   ds
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      """  Global Company field on the GlbCurrRateGrp record to skip  """  
      self.glbRateGrpCode:str = obj["glbRateGrpCode"]
      """  Global Rate Group Code field on the GlbCurrRateGrp record to skip  """  
      self.ds:list[Erp_Tablesets_GlbCurrRateGrpTableset] = obj["ds"]
      pass

class SkipGlbCurrRateGrp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlbCurrRateGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UnlinkGlbCurrRateGrp_input:
   """ Required : 
   glbCompany
   glbRateGrpCode
   ds
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      """  Global Company field on the GlbCurrency record to unlink  """  
      self.glbRateGrpCode:str = obj["glbRateGrpCode"]
      """  Global Rate Group Code field on the GlbCurrRateGrp record to unlink  """  
      self.ds:list[Erp_Tablesets_GlbCurrRateGrpTableset] = obj["ds"]
      pass

class UnlinkGlbCurrRateGrp_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CurrRateGrpTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlbCurrRateGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCurrRateGrpTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCurrRateGrpTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CurrRateGrpTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CurrRateGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateAltCrossCurrCode_input:
   """ Required : 
   plRateGrpCode
   plCrossRate
   proposedAltCrossRate
   """  
   def __init__(self, obj):
      self.plRateGrpCode:str = obj["plRateGrpCode"]
      """  The RateGrpCode selected by the user  """  
      self.plCrossRate:str = obj["plCrossRate"]
      """  The CrossCurrCode selected by the user  """  
      self.proposedAltCrossRate:str = obj["proposedAltCrossRate"]
      """  The AltCrossCurrCode selected by the user  """  
      pass

class ValidateAltCrossCurrCode_output:
   def __init__(self, obj):
      pass

class ValidateBaseRateGrp_input:
   """ Required : 
   plRateGrpCode
   proposedBaseRateGrp
   plCrossCurrCode
   plAltCrossCurrCode
   """  
   def __init__(self, obj):
      self.plRateGrpCode:str = obj["plRateGrpCode"]
      """  The proposed value for Rate Grp  """  
      self.proposedBaseRateGrp:str = obj["proposedBaseRateGrp"]
      """  The proposed value for Base Rate Grp field  """  
      self.plCrossCurrCode:str = obj["plCrossCurrCode"]
      """  The proposed value for CrossCurrCode field  """  
      self.plAltCrossCurrCode:str = obj["plAltCrossCurrCode"]
      """  The proposed value for AltCrossCurrCode field  """  
      pass

class ValidateBaseRateGrp_output:
   def __init__(self, obj):
      pass

class ValidateCrossCurrCode_input:
   """ Required : 
   plRateGrpCode
   proposedCrossRate
   plAltCrossRate
   """  
   def __init__(self, obj):
      self.plRateGrpCode:str = obj["plRateGrpCode"]
      """  The RateGrpCode selected by the user  """  
      self.proposedCrossRate:str = obj["proposedCrossRate"]
      """  The CrossCurrCode selected by the user  """  
      self.plAltCrossRate:str = obj["plAltCrossRate"]
      """  The AltCrossCurrCode selected by the user  """  
      pass

class ValidateCrossCurrCode_output:
   def __init__(self, obj):
      pass

class ValidateCurrencies_input:
   """ Required : 
   plRateGrpCode
   plBaseRateGrp
   proposedCrossRate
   proposedAltCrossRate
   """  
   def __init__(self, obj):
      self.plRateGrpCode:str = obj["plRateGrpCode"]
      """  The RateGrpCode  """  
      self.plBaseRateGrp:str = obj["plBaseRateGrp"]
      """  The Base Rate Group  """  
      self.proposedCrossRate:str = obj["proposedCrossRate"]
      """  The AltCrossCurrCode selected by the user  """  
      self.proposedAltCrossRate:str = obj["proposedAltCrossRate"]
      """  The AltCrossCurrCode selected by the user  """  
      pass

class ValidateCurrencies_output:
   def __init__(self, obj):
      pass

class ValidateInactive_input:
   """ Required : 
   plRateGrpCode
   proposedInactive
   plCrossCurrCode
   plAltCrossCurrCode
   plBaseRateGrpCode
   """  
   def __init__(self, obj):
      self.plRateGrpCode:str = obj["plRateGrpCode"]
      """  The RateGrpCode selected by the user  """  
      self.proposedInactive:bool = obj["proposedInactive"]
      """  The proposed value for Inactive field  """  
      self.plCrossCurrCode:str = obj["plCrossCurrCode"]
      """  The current Cross Rate Currency  """  
      self.plAltCrossCurrCode:str = obj["plAltCrossCurrCode"]
      """  The current Alternative Cross Rate Currency  """  
      self.plBaseRateGrpCode:str = obj["plBaseRateGrpCode"]
      """  The current Base Rate Group  """  
      pass

class ValidateInactive_output:
   def __init__(self, obj):
      pass

class ValidateRateGrpCode_input:
   """ Required : 
   proposedRateGrpCode
   """  
   def __init__(self, obj):
      self.proposedRateGrpCode:str = obj["proposedRateGrpCode"]
      """  The RateGrpCode selected by the user  """  
      pass

class ValidateRateGrpCode_output:
   def __init__(self, obj):
      pass

class ValidateRateGrpDescription_input:
   """ Required : 
   plRateGrpCode
   proposedDescription
   """  
   def __init__(self, obj):
      self.plRateGrpCode:str = obj["plRateGrpCode"]
      """  RateGrpCode value  """  
      self.proposedDescription:str = obj["proposedDescription"]
      """  The Rate group description  """  
      pass

class ValidateRateGrpDescription_output:
   def __init__(self, obj):
      pass

class ValidateRateNumDec_input:
   """ Required : 
   plRateGrpCode
   proposedRateNumDec
   """  
   def __init__(self, obj):
      self.plRateGrpCode:str = obj["plRateGrpCode"]
      """  The RateGrpCode selected by the user  """  
      self.proposedRateNumDec:int = obj["proposedRateNumDec"]
      """  The RateNumDec  """  
      pass

class ValidateRateNumDec_output:
   def __init__(self, obj):
      pass

class ValidateRuleCode_input:
   """ Required : 
   plRateGrpCode
   plUseBaseRate
   plSourceCurrCode
   plTargetCurrCode
   proposedRuleCode
   """  
   def __init__(self, obj):
      self.plRateGrpCode:str = obj["plRateGrpCode"]
      self.plUseBaseRate:bool = obj["plUseBaseRate"]
      self.plSourceCurrCode:str = obj["plSourceCurrCode"]
      self.plTargetCurrCode:str = obj["plTargetCurrCode"]
      self.proposedRuleCode:int = obj["proposedRuleCode"]
      pass

class ValidateRuleCode_output:
   def __init__(self, obj):
      pass

class ValidateUseBaseRate_input:
   """ Required : 
   plRateGrpCode
   proposedUseBaseRate
   """  
   def __init__(self, obj):
      self.plRateGrpCode:str = obj["plRateGrpCode"]
      self.proposedUseBaseRate:bool = obj["proposedUseBaseRate"]
      pass

class ValidateUseBaseRate_output:
   def __init__(self, obj):
      pass

class validateExCurrStatusForRateType_input:
   """ Required : 
   linkGlbCurrRateGrp
   glbRateGrpCode
   """  
   def __init__(self, obj):
      self.linkGlbCurrRateGrp:str = obj["linkGlbCurrRateGrp"]
      """  Link Rate Group Code  """  
      self.glbRateGrpCode:str = obj["glbRateGrpCode"]
      """  Global Rate Group Code  """  
      pass

class validateExCurrStatusForRateType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

